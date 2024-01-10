import React, { useReducer, useEffect } from 'react';
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

const initialState = {
  "status": "Close"
}

function toggleStatus(status,obj){
  let newState;
  newState = obj;
  return newState;
}

function OpenButton({changeFunction}){
  return (
      <button onClick={() => changeFunction({"status": "Open"})}>Open</button>
  )
  }

  function CloseButton({changeFunction}){
  return (
      <button onClick={() => changeFunction({"status": "Close"})}>Close</button>
  )
  }

  function App() {
  const [status, dispatcher] = useReducer(toggleStatus, initialState )
  return ( 
  <>
      <h1>{status.status}</h1>
      <OpenButton changeFunction={dispatcher}/>
      <CloseButton changeFunction={dispatcher}/>
  </>
  )
  }
// function OpenButton({setStatus}){
//   return (
//       <button onClick={() => setStatus("Open")}>Open</button>
//   )
//   }

//   function CloseButton({setStatus}){
//   return (
//       <button onClick={() => setStatus("Close")}>Close</button>
//   )
//   }

//   function App() {
//   const [status, setStatus] = useState("Open")
//   return ( 
//   <>
//       <h1>{status}</h1>
//       <OpenButton setStatus={setStatus}/>
//       <CloseButton setStatus={setStatus}/>
//   </>
//   )
//   }


ReactDOM.render(
  <App />,
  document.getElementById('root')
);
