import React from 'react'


const TodoItem = ({todo}) => {
   return (
       <tr>
           <td>{todo.id}</td>
           <td>{todo.project}</td>
           <td>{todo.user}</td>
           <td>{todo.text}</td>
           <td>{todo.created}</td>
           <td>{todo.updated}</td>
        </tr>
   )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <th>ID</th>
            <th>Project</th>
            <th>User</th>
            <th>Text</th>
            <th>Creared</th>
            <th>Updated</th>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
 }
 
 
 export default TodoList