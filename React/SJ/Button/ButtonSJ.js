import Radium from "radium";

let ButtonSj = ({
  color = "#fff",
  background = "#00427a",
  border = 2,
  width = 150,
  fontSize = 20,
  borderRadius = 8,
  padding = 5,
  fontWeight = 600,
  transform = null,
  startIcon = null,
  endIcon = null,
  height = 43,

  loading = false,
  disabled = false,
  ...props
}) => {
  const styles = {
    position: "relative",
    overflow: "hidden",
    color: color,
    background: background,
    border: `${border}px solid ` + color,
    width: width,
    fontSize: fontSize,
    borderRadius: borderRadius,
    padding: padding,
    fontWeight: fontWeight,
    boxShadow: "0px 8px 15px rgba(0, 0, 0, 0.05)",
    transition: "all 0.3s ease 0s",
    height: height,

    ":disabled": {
      filter: "brightness(.8)",
    },
    ":hover": {
      cursor: "pointer",
      filter: "brightness(1.05)",
      transform: `translateY(${transform}px)`,
    },
    ":active": {
      filter: "brightness(1.3)",
    },
  };
  //ripple effect function
  function createRipple(event) {
    const button = event.currentTarget;

    const circle = document.createElement("span");
    const diameter = Math.max(button.clientWidth, button.clientHeight);
    const radius = diameter / 2;

    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
    circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
    circle.classList.add("ripple");

    const ripple = button.getElementsByClassName("ripple")[0];

    if (ripple) {
      ripple.remove();
    }

    button.appendChild(circle);
  }
  //ripple effect function

  return (
    <button
      style={styles}
      onClick={(e) => {
        props.onClick();
        createRipple(e);
      }}
      disabled={disabled ? true : false}
    >
      {!loading ? (
        props.children ? (
          <span>
            {startIcon}&nbsp;&nbsp;{props.children}&nbsp;&nbsp;{endIcon}
          </span>
        ) : (
          <span>
            {startIcon}
            {endIcon}
          </span>
        )
      ) : (
        <span
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <span
            style={{
              height: styles.fontSize,
              width: styles.fontSize,
              borderRadius: "50%",
              border: "5px solid #00000000",
              borderTop: "5px solid " + styles.color,
              borderRight: "5px solid " + styles.color,
              borderLeft: "5px solid " + styles.color,
              animation: "loading 2s linear infinite",
            }}
          ></span>
          <span style={{ color: styles.color, position: "absolute" }}></span>
        </span>
      )}
    </button>
  );
};

export default Radium(ButtonSj);
