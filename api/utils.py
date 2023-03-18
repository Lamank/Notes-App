from rest_framework.response import Response
from rest_framework import status

from api.models import Note
from api.serializers import NoteSerializer


def getNotesList(request):
    """
    Returns a list of all notes
    """
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=200)


def getNoteDetail(request, pk):
    """
    Returns a single note by id
    """
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data, status=200)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=404)


def createNote(request):
    """
    Creates a new note
    """
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateNote(request, pk):
    """
    Updates a note by id
    """
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    serializer = NoteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def deleteNote(request, pk):
    """
    Deletes a note by id
    """
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)