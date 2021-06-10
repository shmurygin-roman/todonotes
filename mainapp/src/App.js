import React from 'react';
import './App.css';
import axios from 'axios'
import UserList from './components/User.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import TodoList from './components/Todo.js'
import ProjectList from './components/Project.js'
import LoginForm from './components/Auth.js'
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import Cookies from 'universal-cookie'


const NotFound404 = ({ location }) => {
    return (
      <div>
          <h1>Страница по адресу '{location.pathname}' не найдена</h1>
      </div>
    )
  }


class App extends React.Component {
  constructor(props) {
      super(props)
      this.state = {
          'users': [],
          'todo': [],
          'project': [],
          'token': ''
      }
  }


  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token}, ()=>this.load_data())
  }


  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }


  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


  load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/user', {headers})
        .then(response => {
            const users = response.data
                this.setState(
                {
                    'users': users
                }
            )
        }).catch(error => console.log(error))
    
    axios.get('http://127.0.0.1:8000/api/todo', {headers})
        .then(response => {
            const todo = response.data
                this.setState(
                {
                    'todo': todo
                }
            )
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/project', {headers})
        .then(response => {
            const project = response.data
                this.setState(
                {
                    'project': project
                }
            )
        }).catch(error => console.log(error))
  }


  componentDidMount() {
    this.get_token_from_storage()
  }


  render () {
      return (
          <div>
              <BrowserRouter>
                  <Menu>
                      <li><Link to='/user'>Users</Link></li>
                      <li><Link to='/todo'>Todo</Link></li>
                      <li><Link to='/project'>Project</Link></li>
                      <li>{this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}</li>
                  </Menu>
                  <Switch>
                      <Route exact path='/user' component = {() => <UserList users={this.state.users} />} />
                      <Route exact path='/todo' component = {() => <TodoList todos={this.state.todo} />} />
                      <Route exact path='/project' component = {() => <ProjectList projects={this.state.project} />} />
                      <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                      <Redirect from='/' to='/todo' />
                      <Route component={NotFound404} />
                  </Switch>                 
                  <Footer>Footer</Footer>
              </BrowserRouter>
          </div>
      )
  }
}

export default App;
