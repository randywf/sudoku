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

function UploadGrid() {
  return (
    <div>
      <input type="file" name="file" onChange={changeHandler} />
      <div>
        <button onClick={handleSubmission}>Submit</button>
      </div>
    </div>
  )
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
        <button onClick={() => this.newGame()}>New Game{() => this.newGame()}</button>
        UploadGrid()
      </div>
    );
  }
}


ReactDOM.render(<Game />, document.getElementById('root'));