import React, { Component } from "react";
export class TestPage extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return <form>
  <label>
    Title:
    <input type="text" name="title" />
  </label>
            <label>
    Author:
    <input type="text" name="author" />
  </label>
              <label>
    ISBN:
    <input type="text" name="isbn" />
  </label>
  <input type="submit" value="Submit" />
</form>
    }

}