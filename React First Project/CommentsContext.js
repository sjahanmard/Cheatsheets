import React , {createContext, useState} from 'react';
import {v4 as uuid} from 'uuid';
export const CommentContext = createContext();
const CommentContextProvider = (props) => {
    const [comments , setComment] = useState([
        {email: 's.jahanmard@gmail.com',
         text:'Nicest guy eeeeveeer!', id:1},
        {email: 'jahanmard22@gmail.com',
         text:'buffed as f...', id:2}
    ]);
    const addComment = (email,text) =>{
        setComment ([...comments, {email,text,id:uuid()}])
    }
    return (
        <CommentContext.Provider value={{comments , addComment}}>
            {props.children}
        </CommentContext.Provider>
    )
}
export default CommentContextProvider