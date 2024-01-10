# Learning React JS
`Learning React JS - Eve Porcello`

## Chpt. 1
- `create-react-app`
    - command to create SPA with react
    - (2022) requires node v >=~14, so upgrade with nvm ( https://stackoverflow.com/a/12570971 )
    - create app: `npx create-react-app [app_name]`

    ( to `touring a create-react-app project` )

- run app with `npm start`
    

- Contents of generated app
    - `package.json`: contains project dependencies
    - `src` folder contains all the files used to build application
    - `public` folder: where build files will be placed for production

## Chpt. 2 - React ELements
- `React.createElement() `takes three args
    - name of tag to create (eg. "h1")
    - properties that the element should have
        - properties passed in as object
            - eg. { id: "welcome-div", class: "disable-click" }
    - children that the element should have

- Rendering multiple elements
    - can make the "child" argument of a .createElement call another .createElement call, producing nested elements
        - eg. parent .createElement is a <div> , it's child is a .createElement producing an <h1>
        - can also have multiple "child" elements
    - for more complex cases, use JSV
- `JSX`
    - JSX allows to use html-like syntax
    - eg.
        ```
            ReactDOM.render(
                <div>
                    <h1>Hellow World</h1>
                    <p>Tada today</p>
                </div>,
                document.getElementById('root')
            );
        ```
    - requires Babel to compile, which is automatically enabled with app creation
    - allows for dynamic content generation (like fstring in python)
        - eg
            ```
                let city = {
                name: "Madrid",
                country: "Spain"
                };

                ReactDOM.render(
                    <h1 id="heading" className="cool-text">
                        {city.name} is in {city.country}
                    </h1>,
                    document.getElementById("root")
                );
            ```
## Chpt. 3 React Components
- component: collection of react elements ( elements are the most atomic element in react applications )
    - Components are functions returning elements of UI
    - a component is refered to by JSX tag in the render call
        - ! component names must be Capitalized, JSX require this 
    - eg
        ```
        function Hello(){
        return (
            <div>
            <h1>Hellow World</h1>
            <p>yellow world</p>
            </div>
        )
        }

        ReactDOM.render(
        <Hello/>,
        document.getElementById('root')
        );
        ```
- property
    - object in React containing properties about component
        - allow display of dynamic content within component
    - props are added as attribute to the component's tag, can than be used within the component
        - eg. 
        ```
            function Hello(props){
                return (
                    <div>
                    <h1>{props.library} Hellow World</h1>
                    <p>{props.color} world</p>
                    </div>
                )
            }

            ReactDOM.render(
            <Hello library="React" color="yellow"/>,
            document.getElementById('root')
            );
        ```
    - integers must be passed within {}s `<Hello number={1}>`
    - can also use destructuring on props object
        ```
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
        ```
- rendering a list
    - use the `.map()` JS method in curly braces to loop through an array and generate a list
    - eg. 
    ```
    const lakes = ['Elkhart', 'Crystal', 'Michigan']
    ...
    function App(props){
    return(
        <ul>
            {props.lakes.map( lake => <li>{lake}</li>) }
        </ul>
    )
    ...
    }
    ```
- adding keys
    - when rendering a list, each child in the list must have a unique key property
        - `key='[some_uid]'`
    - Can add iterator to .map() function to generate keys
        ```

            function App( { items } ){<--destructured from props object
                return(
                    {items.map((item, i) => (
                        <div key={i}>{item}</div>
                    ))}
                )
            }
        ```
    - can also just use `.toString()` to create a key based on the value being rendered
        ```
            function App( { items } ){<--destructured from props object
                return(
                    {items.map( item => (
                        <div key={item.toString()}>{item}</div>
                    ))}
                )
            }
        ```
- React Fragments
    - if you have an App function returning two or more components, they either must be wrapped in an enclosing tag, or you can use React fragments
    - either `React.Fragment` tags or just `<> and </>`
    - eg. 

    function App(){
        render(
            <React.Fragment>
                <Component1 />
                <Component2 />
            </React.Fragment>
        )
    } 
    - prevents clutter from having to wrap everything in <div> tags


## Chpt. 4 React State with Hooks
- array destructuring
    - can set variable names for items in an array, so don't have to refer to by index
    - eg. 
    ```
        const arr = [1, 2, 3]
        const [ one, two ] = arr
        console.log(one, two) -(print)>> '1 2'
    ```
    - if only want to name one item in array, use commas for placeholders
    ```
    const arr = [1, 2, 3]
    const[, , three] = arr
    console.log(three) -(print)>> '3'
    ```

- useState hook
    - hooks are functions that allow one to add functionality to a component
    - import with `import { useState } from 'react'`
    - the `useState` function returns two things: a status, and a function called `setStatus`
    - eg.
        ```
            function OpenButton({setStatus}){
            return (
                <button onClick={() => setStatus("Open")}>Open</button>
            )
            }

            function CloseButton({setStatus}){
            return (
                <button onClick={() => setStatus("Close")}>Close</button>
            )
            }

            function App() {
            const [status, setStatus] = useState("Open")
            return ( 
            <>
                <h1>{status}</h1>
                <OpenButton setStatus={setStatus}/>
                <CloseButton setStatus={setStatus}/>
            </>
            )
            }
        ```
    - initialize state in the parent component (eg `App` ) and pass the setStatus function to child components

    - using multiple state variables
        - can have multiple implementations of `useState` module, just have to give the set function a unique name (eg. `setStatus`, `setManager`, `setYear` )

- `useEffect` Hook
    - used to have a function do something besides render UI ( fire alert, console.log, etc. ) inside of a React Component

    ( to Updating with the useEffect dependency array )

## Chpt. 5 React Enhancements
- `useEffect` is intended to be used in conjunction with other React stateful hooks like `useState` and `useReducer`
    ```
        function App(){
            const [ fn, setFn ] = useState( "" )
            const [ ln, setLn ] = useState( "" )

            useEffect( () => {
                console.log(`First Name: ${fn}`)
                console.log(`Last Name: ${ln}`)
            })
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
    ```
    - second argument sent to `useEffect` is the dependency array; We can give the state variables that we want to listen for changes in here; otherwise, useEffect fire on change anywhere 
        ```
            useEffect( () => {
                console.log(`First Name: ${fn}`)
            }, [fn])
        ```
        - fires only on change to `fn` state variable

- `useReducer` hook
    - reducers take in one state and return another
    - useReducer takes as arguments: a reducer function and the initial state
    ```
        const initialState = {count: 0};

        function reducer(state, action) {
        switch (action.type) {
            case 'increment':
            return {count: state.count + 1};
            case 'decrement':
            return {count: state.count - 1};
            default:
            throw new Error();
        }
        }

        function Counter() {
        const [state, dispatch] = useReducer(reducer, initialState);
        return (
            <>
            Count: {state.count}
            <button onClick={() => dispatch({type: 'decrement'})}>-</button>
            <button onClick={() => dispatch({type: 'increment'})}>+</button>
            </>
        );
        }
    ```