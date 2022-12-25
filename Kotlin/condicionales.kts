
var calif = put_calificacion()
var redondeado = redondear_calif(calif)
var aprobado = aprobadoOrNot(redondeado)
print("El estudiante está ${aprobado}")

fun put_calificacion() : Double {
    print("Ingresa la calificacion entre 0 y 10: ")
    var calif = readLine()!!.toDouble()
    return calif
}

fun redondear_calif(cal : Double) : Double {
    var redondeado : Int = cal.toInt()
    if (cal > redondeado ){
        redondeado++
    }
    return redondeado.toDouble()
}

fun aprobadoOrNot(redondeado : Double) : String {
    var aprobado : String
    if (redondeado < 6){
        aprobado = "Reprobado"
    }else{
        aprobado = "Aprobado"
    }
    return aprobado
}