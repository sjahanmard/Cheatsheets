import React from 'react';
import  { CommentContext } from './CommentsContext';

const CommentDetail = ({comment}) => {
    return(
        <li>
            <p>{comment.email}</p>
            <h2>{comment.text}</h2>
        </li>
    );
}
export default CommentDetail