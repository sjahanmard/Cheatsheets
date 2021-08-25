import logo from "./logo.svg";
import "./App.css";
import Component from "./components/component";
import withVariable from "./components/withVariable";
const Dudu = withVariable(Component);

function App() {
  return (
    <div className="App">
      <Dudu />
    </div>
  );
}

export default App;
