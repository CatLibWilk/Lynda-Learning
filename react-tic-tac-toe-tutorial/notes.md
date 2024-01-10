# tutorial at https://reactjs.org/tutorial/tutorial.html

## Setup
- `npx create-react-app [appname]`
- `cd` into the app directory and start with `npm start`

## Passing props to components
- props passed from parent to child
```
    class Board extends React.Component {
    renderSquare(i) {
        return <Square value={i} />;  }
    }

    class Square extends React.Component {
    render() {
        return (
        <button className="square">
            {this.props.value}     
        </button>
        );
    }
    }
```

## state
- define `this.state` in the react components constructor
    ```
    class Square extends React.Component {
        constructor(props) {    
            super(props);    
            this.state = {      
                value: null,    
            };  
    }
    ...
    ```
- `this.state` should be private to the component

- can update component's state with the `this.setState()` method. 
    - using setState will make the component rerender every time it's called
        - will also trigger rerender of any children components

- React will update only the properties mentioned in setState method leaving the remaining state as is
    - eg. if state has three properties
        ```
            state = {
                currentUser: 0,
                number: 0,
                isActive: False
            }
        ```
        - and you do 
        ```
            this.setState({
                isActive: True
            })
        ```
        - state will now be:
        ```
            {
                currentUser: 0,
                number: 0,
                isActive: True
            }
        ```
## Lifting up state
- shared state should be stored in parent component
- define state in parent and then pass a function for setting state down to the child component
```
    class Parent extends React.Component{
        constructor(props){
            super(props);
            this.state = {      
            squares: Array(9).fill(null),    
            };  
        }

        handleClick(i) {
            const squares = this.state.squares.slice();<-------this creates a copy of the state array, for mutability
            squares[i] = 'X';    
            this.setState({squares: squares});  
        }

        render(){
            return(
                <Child 
                    value={this.state.squares[i]} 
                    onClick={()=>{
                        this.handleClick(i)
                    }}
                />
            )
        }
    }

    class Child extends React.Component{
        render() {
            return (
                <button onClick={ ( )=>{ this.props.onClick() } }>
                {this.props.value}
                </button>
            );
        }
    }
```

- immutability is important because it's easier to determine if a data object has changed, eg. in order to determine if an update has occured and component needs to be rerendered. 
    - difference between having to compare two versions of the data object and see if different (mutable approach) vs. the object being refered to by a variable declaration is different (immutable approach)

    - example
        ```
            const squares = this.state.squares.slice(); <----- slice with no arg just makes a copy of the array
            this.setState(
                {
                squares: squares,
                xIsNext: !this.state.xIsNext
                }
            );  
        ```

- adding revert state
    - because changing data with immutablility, can store state before each change
    - in the Game (parent) component, state will now be `history` and `xIsNext`
        ```
            this.state = {      
                history: [{        
                    squares: Array(9).fill(null),      
                }],      
                xIsNext: true,    
            };
        ```
    - the Game components `render` function will use most recent `history` state entry for rendering the board
        ```
            const history = this.state.history;    
            const current = history[history.length - 1];
            ...
            return(){
                ...
                <Board            
                    squares={current.squares}            
                    onClick={(i) => this.handleClick(i)}          
                />
                ...
            }
        ```
    - handleClick (now in Game component as well) will concatenate new history entries on to `history` state
        ```

        handleClick(i) {
            const history = this.state.history;    
            const current = history[history.length - 1];    
            const squares = current.squares.slice();    
            if (calculateWinner(squares) || squares[i]) {
                return;
            }
            squares[i] = this.state.xIsNext ? 'X' : 'O';
            this.setState({
                history: history.concat([{        
                    squares: squares,      
                    }]),     
                xIsNext: !this.state.xIsNext,
            });
        }
        ```

    - Using the map method, can map history of moves to React elements representing buttons on the screen, and display a list of buttons to “jump” to past moves
        ```
            const history = this.state.history;   
            const current = history[this.state.stepNumber] 
            const winner = calculateWinner(current.squares);    

            const moves = history.map((step, move) => {      
                const desc = move ? 'Go to move #' + move : 'Go to game start';
                return (
                    <li key={move}>          
                    <button onClick={() => this.jumpTo(move)}>{desc}</button>        
                    </li>      
                );
            });
        ```

( to "Wrapping Up" )