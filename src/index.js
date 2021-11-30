import { render } from '@testing-library/react';
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

// CSS class names for the different cell types in the grid
const classNameMap = {
  0:['cellTopLeft','cellTopCenter','cellTopRight'],
  1:['cellCenterLeft','cellCenter','cellCenterRight'],
  2:['cellBottomLeft','cellBottomCenter','cellBottomRight']
};

// Initialize an empty sudoku grid as a 2d array
const initialGridState = new Array(9).fill("").map(() => new Array(9).fill(""))


class Cell extends React.Component {
  constructor(props) {
    super(props);
    this.onKeyDown = this.onKeyDown.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  onKeyDown(event) {
    // Allow backspace
    if (event.key === "Backspace") {
      console.log("Cell %s: Backspace pressed", this.props.id);
      this.props.onChangeCellValue(event)
    }
    else if (/^[1-9]/.test(event.key)) {
      console.log("Cell %s: %s entered", this.props.id, event.key);
      //this.props.onChangeCellValue(event);
    }
    else {
      console.log("Cell %s: Key press unrecognized (%s)", this.props.id, event.key);
    }
  }

  handleChange(event) {
    // Change value if 1-9 is entered
    console.log("Cell %s: Change event", this.props.id);
    this.props.onChangeCellValue(event);
  }

  handleSubmit(event) {
    // Don't allow form submission
    event.preventDefault();
  }

  render() {
    console.log("Rendering cell %s", this.props.id)
    if (this.props.fixed) {
      return (
        <p className='fixedCellContent'>{this.props.value}</p>
      );
    } else {
      return (
        <form onSubmit={this.handleSubmit}>
          <input 
            id={this.props.id}
            className='cellContent'
            type='text' 
            value={this.props.value}
            onChange={this.handleChange} 
            onKeyDown={this.onKeyDown}
          />
        </form>
      );
    }
  }
}


class Grid extends React.Component {
  renderCell(row, col) {
    console.log("RenderCell %s, %s", row, col);
    return (
      <td className={classNameMap[row % 3][col % 3]}>
        <Cell 
          id={row * 9 + col}
          value={this.props.gridState[row][col]}
          onChangeCellValue={this.props.onChangeCellValue}
        />
      </td>
    );
  }

  render() {
    console.log("Rendering grid")
    return (
      <div className='grid'>
        <table className='gridTable'>
          <tbody>
            <tr>
              {this.renderCell(0,0)}
              {this.renderCell(0,1)}
              {this.renderCell(0,2)}
              {this.renderCell(0,3)}
              {this.renderCell(0,4)}
              {this.renderCell(0,5)}
              {this.renderCell(0,6)}
              {this.renderCell(0,7)}
              {this.renderCell(0,8)}
            </tr>
            <tr>
              {this.renderCell(1,0)}
              {this.renderCell(1,1)}
              {this.renderCell(1,2)}
              {this.renderCell(1,3)}
              {this.renderCell(1,4)}
              {this.renderCell(1,5)}
              {this.renderCell(1,6)}
              {this.renderCell(1,7)}
              {this.renderCell(1,8)}
            </tr>
            <tr>
              {this.renderCell(2,0)}
              {this.renderCell(2,1)}
              {this.renderCell(2,2)}
              {this.renderCell(2,3)}
              {this.renderCell(2,4)}
              {this.renderCell(2,5)}
              {this.renderCell(2,6)}
              {this.renderCell(2,7)}
              {this.renderCell(2,8)}
            </tr>
            <tr>
              {this.renderCell(3,0)}
              {this.renderCell(3,1)}
              {this.renderCell(3,2)}
              {this.renderCell(3,3)}
              {this.renderCell(3,4)}
              {this.renderCell(3,5)}
              {this.renderCell(3,6)}
              {this.renderCell(3,7)}
              {this.renderCell(3,8)}
            </tr>
            <tr>
              {this.renderCell(4,0)}
              {this.renderCell(4,1)}
              {this.renderCell(4,2)}
              {this.renderCell(4,3)}
              {this.renderCell(4,4)}
              {this.renderCell(4,5)}
              {this.renderCell(4,6)}
              {this.renderCell(4,7)}
              {this.renderCell(4,8)}
            </tr>
            <tr>
              {this.renderCell(5,0)}
              {this.renderCell(5,1)}
              {this.renderCell(5,2)}
              {this.renderCell(5,3)}
              {this.renderCell(5,4)}
              {this.renderCell(5,5)}
              {this.renderCell(5,6)}
              {this.renderCell(5,7)}
              {this.renderCell(5,8)}
            </tr>
            <tr>
              {this.renderCell(6,0)}
              {this.renderCell(6,1)}
              {this.renderCell(6,2)}
              {this.renderCell(6,3)}
              {this.renderCell(6,4)}
              {this.renderCell(6,5)}
              {this.renderCell(6,6)}
              {this.renderCell(6,7)}
              {this.renderCell(6,8)}
            </tr>
            <tr>
              {this.renderCell(7,0)}
              {this.renderCell(7,1)}
              {this.renderCell(7,2)}
              {this.renderCell(7,3)}
              {this.renderCell(7,4)}
              {this.renderCell(7,5)}
              {this.renderCell(7,6)}
              {this.renderCell(7,7)}
              {this.renderCell(7,8)}
            </tr>
            <tr>
              {this.renderCell(8,0)}
              {this.renderCell(8,1)}
              {this.renderCell(8,2)}
              {this.renderCell(8,3)}
              {this.renderCell(8,4)}
              {this.renderCell(8,5)}
              {this.renderCell(8,6)}
              {this.renderCell(8,7)}
              {this.renderCell(8,8)}
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}


class FileControls extends React.Component {
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
      <div className="fileControls">
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
    // Give a random suggestion for filling a square
    console.log("Hint");
  }

  onGameSubmit() {
    // Submit game to backend server for scoring and validation
    console.log("Submit Game")
  }

  render() {
    return (
      <div className="gameControls">
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
    this.state = {
      gridState: initialGridState
    };
    this.onChangeCellValue = this.onChangeCellValue.bind(this);
  }

  changeCellValue(row, col, val) {
    this.setState({
     gridState: this.state.gridState.map((rowElement, rowIndex) => {
       return rowElement.map((columnElement, columnIndex) => {
          if (rowIndex === row && columnIndex === col) {
            return val;
          } else {
            return columnElement;
          }
        });
      })
    });
  }
  
  onChangeCellValue(event) {
    let row = Math.floor(event.target.id / 9);
    let col = event.target.id % 9;
    let new_value = event.target.value.substr(-1)
    if (event.key == "Backspace") {
      this.changeCellValue(row, col, "");
    } else if (/^[1-9]/.test(new_value)) {
      this.changeCellValue(row, col, new_value);
    }
  }

  render() {
    return (
      <div>
        <Grid
          gridState={this.state.gridState} 
          onChangeCellValue={(e) => this.onChangeCellValue(e)}
        />
        <GameControls />
        <FileControls />
      </div>
    );
  }
}


ReactDOM.render(<Game />, document.getElementById('root'));