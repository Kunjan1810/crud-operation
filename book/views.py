# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from .models import Book

class BookAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                data = {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'published_date': book.published_date,
                    'isbn': book.isbn,
                    'pages': book.pages,
                    'cover': book.cover,
                    'language': book.language,
                }
                return Response(data, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            books = Book.objects.all()
            data = [
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'published_date': book.published_date,
                    'isbn': book.isbn,
                    'pages': book.pages,
                    'cover': book.cover,
                    'language': book.language,
                }
                for book in books
            ]
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        try:
            book = Book.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                published_date=data.get('published_date'),
                isbn=data.get('isbn'),
                pages=data.get('pages'),
                cover=data.get('cover'),
                language=data.get('language'),
            )
            return Response({'id': book.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({'error': 'Book ID required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=pk)
            data = request.data
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.published_date = data.get('published_date', book.published_date)
            book.isbn = data.get('isbn', book.isbn)
            book.pages = data.get('pages', book.pages)
            book.cover = data.get('cover', book.cover)
            book.language = data.get('language', book.language)
            book.save()
            return Response({'message': 'Book updated'}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': 'Book ID required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({'message': 'Book deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
