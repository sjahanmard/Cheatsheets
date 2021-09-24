import Scrollbar from "./Scrollbar";

function App() {
  const label = "this is the first test";
  const items = [
    { value: "lambo", showing: "LAMBO" },
    { value: "bmw", showing: "BMW" },
    { value: "bmw", showing: "BMW" },
    { value: "bmw", showing: "BMW" },
    { value: "bmw", showing: "BMW" },
  ];

  return (
    <div className="App">
      <Scrollbar
        label={label}
        items={items}
        colors={{ textColor: "white", backColor: "blue" }}
      />
    </div>
  );
}

export default App;
