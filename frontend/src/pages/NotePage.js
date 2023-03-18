import React, {useState, useEffect} from 'react'
import { useNavigate, useParams } from 'react-router-dom';
import { ReactComponent as ArrowLeft} from '../assets/arrow-left.svg';

const NotePage = (history) => {
  
  let {id} = useParams();
  let [note, setNote] = useState();
  const navigate = useNavigate();

    useEffect(() => {
        getNote();
    }, [id]);

    let getNote = async ()=>{
      if (id === 'new') return
      let response = await fetch(`/api/notes/${id}/`);
      let data = await response.json();

      setNote(data);
    };

    let createNote = async ()=>{
      let response = await fetch(`/api/notes/`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(note)
      });
      let data = await response.json();

      setNote(data);
    };

    let updateNote = async ()=>{
      let response = await fetch(`/api/notes/${id}/`,{
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(note)
      });
      let data = await response.json();

      setNote(data);
    };
    
    let deleteNote = async () =>{
      await fetch(`/api/notes/${id}/`,{
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
      });
      setNote(null);
      navigate(`/`);
    }

    let handleSubmit = async () => {
      if(id !== 'new' && note.body === ''){
        deleteNote();
      }
      else if(id !== 'new'){
        await updateNote();
      }
      else if(id === 'new' && note.body !== null){
        await createNote();
      }
      navigate(-1);
    };

  

    let handleChange = (value) => {
      setNote(note => ({...note, 'body':value}));
    };

  return (
    <div className='note'>
      <div className='notes-header'>
        <h3>
          <ArrowLeft onClick={handleSubmit} />
        </h3>
        {id !== 'new' ? (
           <button onClick={deleteNote} className='btn-style'>Delete</button>
        ): (
          <button className='btn-style' onClick={handleSubmit}>Done</button>
        )
        }
       
      </div>
      <textarea onChange={(e) => {handleChange(e.target.value)}} value={note?.body}></textarea>
    </div>
  )
}

export default NotePage
