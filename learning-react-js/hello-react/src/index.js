import React from 'react';
import './index.css';
import ReactDOM from 'react-dom';

// ReactDOM.render(
// React.createElement( "div", 
//   { id: "welcome-div", class: "disable-click" }, 
//     React.createElement( 'h1', { id: 'title' }, "Hello World" ), 
//     React.createElement( 'p', { id: 'text' }, "Welcome" ), 
//   ),
//   document.getElementById('root')
// );

function Hello({library, color}){
  return (
    <div>
      <h1>{library} Hellow World</h1>
      <p>{color} world</p>
    </div>
  )
}


ReactDOM.render(
  <Hello library="React" color="yellow" />,
  document.getElementById('root')
);
