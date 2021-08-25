import logo from "./logo.svg";
import "./App.css";
import Component from "./components/Component";
import withVariable from "./components/withVariable";
const EnhancedComponent = withVariable(Component);

function App() {
  return (
    <div className="App">
      <EnhancedComponent lastname="jahanmard" />
    </div>
  );
}

export default App;
