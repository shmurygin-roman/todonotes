import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import UserList from './components/User.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import TodoList from './components/Todo.js'
import ProjectList from './components/Project.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


class App extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
          'users': [],
          'todo': [],
          'project': []
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
    
    axios.get('http://127.0.0.1:8000/api/todo')
        .then(response => {
            const todo = response.data
                this.setState(
                {
                    'todo': todo
                }
            )
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/project')
        .then(response => {
            const project = response.data
                this.setState(
                {
                    'project': project
                }
            )
        }).catch(error => console.log(error))
  }


  render () {
      return (
          <div>
              <BrowserRouter>
                  <Menu>
                      <li><Link to='/user'>Users</Link></li>
                      <li><Link to='/todo'>Todo</Link></li>
                      <li><Link to='/project'>Project</Link></li>
                  </Menu>
                  <Switch>
                      <Route exact path='/user' component = {() => <UserList users={this.state.users} />} />
                      <Route exact path='/todo' component = {() => <TodoList todos={this.state.todo} />} />
                      <Route exact path='/project' component = {() => <ProjectList projects={this.state.project} />} />
                  </Switch>                 
                  <Footer>Footer</Footer>
              </BrowserRouter>
          </div>
      )
  }
}

export default App;
