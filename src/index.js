import { render } from '@testing-library/react';
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Cell extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };
    // Controlled component
    this.onKeyDown = this.onKeyDown.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  onKeyDown(event) {
    // Allow backspace
    if (event.keyCode === 8) {
      this.setState({value: ''});
    }
  }

  handleChange(event) {
    // Change value if 1-9 is entered
    let new_value = event.target.value.substr(-1)
    if (/^[1-9]/.test(new_value)) {
      this.setState({value: new_value});
    }
  }

  handleSubmit(event) {
    // Don't allow form submission
    event.preventDefault();
  }

  render() {
    if (this.props.fixed) {
      return (
        <td className={this.props.className}>{this.state.value}</td>
      );
    }
    else {
      return (
        <td className={this.props.className}>
          <form onSubmit={this.handleSubmit}>
            <input 
              className='cellContent'
              type='text' 
              value={this.state.value} 
              onChange={this.handleChange} 
              onKeyDown={this.onKeyDown}
            />
          </form>
        </td>
      );
    }
  }
}


class Grid extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      rows: []
    };
    let classNameMap = {
      0:['cellTopLeft','cellTopCenter','cellTopRight'],
      1:['cellCenterLeft','cellCenter','cellCenterRight'],
      2:['cellBottomLeft','cellBottomCenter','cellBottomRight']
    };
    for (let row = 0; row < 9; row++) {
      let cells = []
      for (let col = 0; col < 9; col++) {
        let cellID = row * 9 + col
        cells.push(<Cell 
          key={cellID} 
          id={cellID} 
          className={classNameMap[row % 3][col % 3]}
        />);
      }
      this.state.rows.push(<tr key={row}>{cells}</tr>)
    }
  }

  render() {
    return (
      <div className='grid'>
        <table className='grid'>
          <tbody>
            {this.state.rows}
          </tbody>
        </table>
      </div>
    )
  }
}


function NewGame() {
  return('');
}

class UploadGrid extends React.Component {
  state = {
    selectedFile: null
  };

  onFileSelect = event => {
    this.setState({ selectedFile: event.target.files[0] });
  }

  onFileSubmit = () => {
    console.log("Uploading: " + this.state.selectedFile);
  }

  render() {
    return (
      <div>
        <input type="file" name="file" onChange={this.onFileSelect} />
        <div>
          <button onClick={this.onFileSubmit}>Upload</button>
        </div>
      </div>
    );
  }
}


class GameControls extends React.Component {
  onGameNew() {
    // Request a new grid from the backend server
    console.log("New game");
  }

  onGameCheck() {
    // Check grid to see if sudoku is solved
    console.log("Check game");
  }

  onGameHint() {
    // Give a random hint (suggestion for filling a square)
    console.log("Hint");
  }

  onGameSubmit() {
    // Submit game to backend server for scoring and validation
    console.log("Submit Game")
  }

  render() {
    return (
      <div className="gameControls" align="center">
        <table>
          <tbody>
            <tr>
              <td>
                <button onClick={this.onGameNew}>New Game</button>
              </td>
              <td>
                <button onClick={this.onGameCheck}>Check</button>
              </td>
              <td>
                <button onClick={this.onGameHint}>Hint</button>
              </td>
              <td>
                <button onClick={this.onGameSubmit}>Submit</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    )
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
  }

  newGame() {
    return "";
  }

  render() {
    return (
      <div>
        <Grid />
        <GameControls />
        <UploadGrid />
      </div>
    );
  }
}


ReactDOM.render(<Game />, document.getElementById('root'));