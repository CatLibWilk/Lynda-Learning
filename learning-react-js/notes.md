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
( to `Composing Components` )