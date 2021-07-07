import React, {useState,useContext} from 'react'
import { CommentContext } from './CommentsContext'
const CommentForm = () => {
    const [email, setEmail] = useState('')
    const [text,setText] = useState('')
    const{addComment} = useContext(CommentContext)
    const handleSubmit = (e) => {
        e.preventDefault();
        addComment(email, text)
        setEmail('')
        setText('')
    }
    return (
        <form onSubmit={handleSubmit}>
            <input type='email' placeholder ='Email' value={email} required
                onChange={(e)=>setEmail(e.target.value)}/>
            <textarea type='textarea'placeholder ='Your Comment' value={text} required
                  onChange={(e)=>setText(e.target.value)}/>
            <input type='submit' value='Press To Submit'/>

        </form>
    );
}
export default CommentForm;