const Scrollbar = ({
  label = "just some label",
  items,
  colors = {
    textColor: "red",
    backColor: "green",
  },
}) => {
  console.log(items);
  let showing = items.map((item, i) => {
    console.log(item, i);
    return (
      <option key={i} value={item.value}>
        {item.showing}
      </option>
    );
  });
  console.log(showing);
  return (
    <div
      style={{
        textAlign: "start",
        color: colors.textColor,
        background: colors.backColor,
        width: 200,
      }}
    >
      <label>{label}:</label>

      <select name="cars" id="cars">
        {showing}
      </select>
    </div>
  );
};

export default Scrollbar;
