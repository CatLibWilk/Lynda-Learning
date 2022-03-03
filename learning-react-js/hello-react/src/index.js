import React, { useState, useEffect } from 'react';
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

function App(){
  const [ fn, setFn ] = useState( "" )
  const [ ln, setLn ] = useState( "" )

  useEffect( () => {
    console.log(`First Name: ${fn}`)
  }, [fn])

  useEffect( () => {
    console.log(`Last Name: ${ln}`)
  }, [ln])
  return (
    <>
    <br></br>
    <label>
      First Name:
      <input value={fn} onChange={e => setFn(e.target.value)}/>
    </label>
    <br/>
    <br/>
    <label>
      Last Name:
      <input value={ln} onChange={e => setLn(e.target.value)}/>
    </label>
    </>
  )
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
);
