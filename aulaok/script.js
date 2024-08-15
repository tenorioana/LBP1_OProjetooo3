console.log("Script Carregado");
function calcularAnos(){
    console.log("Botão de calcular clicando");

    let popAInput = document.getElementById("popA").value.trim();

    let taxaAINput = document.getElementById("taxaA").value.trim();

    let popBInput = document.getElementById("popB").value.trim();

    let taxaBINput = document.getElementById("taxaB").value.trim();

    if (popAInput === "" || taxaAINput=== "" || popBInput === "" || taxaBINput === "")
        alert("Por favor, preencah todos os campos");
    return;
    

}