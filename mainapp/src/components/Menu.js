var style = {
    backgroundColor: "#F8F8F8",
    borderTop: "1px solid #E7E7E7",
    textAlign: "center",
    padding: "10px",
    height: "30px",
    width: "100%",
}


function Menu({ children }) {
    return (
        <div>
            <div style={style}>
                { children }
            </div>
        </div>
    )
}

export default Menu