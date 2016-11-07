
//-------------React File for handling Home Page-----------------//
import React from 'react';
import ReactDOM from 'react-dom'
// import { Router, Route, Link, hashHistory, IndexRoute } from 'react-router'
import { Button, ButtonToolbar, ButtonGroup, Grid, Row, Col } from 'react-bootstrap'
import { Form, FormGroup, FormControl } from 'react-bootstrap'



ReactDOM.render( <Form />, document.getElementById('form'));


//-----------New Mail Form----------------//
var Form = React.createClass({
  getInitialState: function() {
    return {subject: '', to: '', date: '', id: '', url: '/api/goal/'};
  },

  handleNameChange: function(e) {
    this.setState({name: e.target.value});
  },

  handleTextChange: function(e) {
    this.setState({text: e.target.value});
  },

  handleDateChange: function(e) {
    this.setState({date: e.target.value});
  },

  handleSubmit: function(e) {
    e.preventDefault();
    var name = this.state.name.trim();
    var text = this.state.text.trim();
    var date = this.state.date.trim();
    var id = this.state.id;
    if (!text || !name) {
      return;
    }
    this.handleNewLifeGoal({
      name: name, 
      description:text, 
      end_date:date, 
      id:id})
    this.setState({
      name: '', 
      text: '', 
      date: '', 
      id: '', 
      url: '/api/goal/'});
  },

  handleNewLifeGoal: function(goal) {
    $.ajax({
      url: this.state.url,
      dataType: 'json',
      type: 'POST',
      data: goal,
      success: function(data) {
        this.props.history.pushState(null,'goal_list')
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(status, err.toString());
      }.bind(this)
    });
  },

  // handleGoalUpdate: function(id) {
  //   $.ajax({
  //     url: '/api/update/?id=' + id,
  //     dataType: 'json',
  //     type: 'GET',
  //     success: function(data) {
  //       this.setState({
  //         name: data.name,
  //         text: data.text,
  //         date: data.end_date,
  //         id: data.id,
  //         url: '/api/update/'
  //       })
  //     }.bind(this),
  //     error: function(xhr, status, err) {
  //       console.error(status, err.toString());
  //     }.bind(this)
  //   });
  // },

  // componentWillReceiveProps: function(nextProps) {
  //   if (nextProps.params.fill != 'null') {
  //     this.handleGoalUpdate(nextProps.params.fill)
  //   }
  // },

  render: function() {
    var buttonStyle = {
        backgroundColor: "#f9f9f9",
        borderRadius: 10,
        border: "2px solid #dcdcdc",
        display: "inline-block",
        color: "#666666",
        fontSize: "18",
        fontWeight: "bold",
        padding: "8px 12px 8px 12px",
        margin: "15px 5px 15px 5px",
    }
    var textStyle = {
      fontFamily: "Josefin Sans",
    }
    return (
      <Form style= {textStyle} 
            horizontal className="newGoal" 
            onSubmit={this.handleSubmit}>
        <FormGroup controlId="formHorizontalName">
          <Col componentClass="text" xs={3}>
            Goal Name
          </Col>
          <Col xs={9}>
            <FormControl 
              name = "name"
              type="text" 
              placeholder= "Your Life Goal name"
              value={this.state.name}
              onChange={this.handleNameChange} />
          </Col>
        </FormGroup>

        <FormGroup controlId="formHorizontalDate">
          <Col componentClass="date" xs={3}>
            End Date
          </Col>
          <Col xs={9}>
            <FormControl 
              name = "end_date"
              type="date" 
              placeholder="Ends on [YYYY-MM-DD]"
              value={this.state.date}
              onChange={this.handleDateChange} />
          </Col>
        </FormGroup>

        <FormGroup controlId="formHorizontalDescription">
          <Col xs={3}>
            Description
          </Col>
          <Col xs={9}>
            <FormControl 
              name = "description"
              componentClass="textarea"
              placeholder="Say something..."
              value={this.state.text}
              onChange={this.handleTextChange} />
          </Col>
        </FormGroup>

        <FormGroup>
          <Col xsOffset={5} xs={8}>
            <Button style={buttonStyle} type="submit">
              Submit
            </Button>
          </Col>
        </FormGroup>
      </Form>
    );
  }
});





