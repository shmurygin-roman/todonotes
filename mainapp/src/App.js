import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import axios from 'axios'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


class App extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
          'users': []
      }
  }


  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/user')
        .then(response => {
            const users = response.data
                this.setState(
                {
                    'users': users
                }
            )
        }).catch(error => console.log(error))
  }


  render () {
      return (
          
          <div>
              <Menu>Menu Main App</Menu>
              <UserList users={this.state.users} />
              <Footer>Footer</Footer>
          </div>
      )
  }
}

export default App;
