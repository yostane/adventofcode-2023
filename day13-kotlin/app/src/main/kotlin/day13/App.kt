/*
 * This Kotlin source file was generated by the Gradle 'init' task.
 */
package day13

data class Pattern(val lines: List<String>){

    val columns = lines[0].indices.map { getColumn(it) }
    private fun countRowsBeforeReflection(rows: List<String>): Int {
        for (i in rows.indices){
            for (j in i..<rows.size) {
                if (rows[i] == rows[j]) {
                    return i + (j - i) / 2
                }
            }
        }
        return 0
    }

    private fun getColumn(column: Int): String {
        val sb = StringBuilder()
        for(i in lines.indices){
            sb.append(lines[i][column])
        }
        return sb.toString()
    }

    fun countColumnsBeforeReflectionColumn(): Int {
        return countRowsBeforeReflection(columns)
    }

    fun countLinesBeforeReflection(): Int {
        return countRowsBeforeReflection(lines)
    }
}


class App(input: String) {
    val patterns: List<Pattern> = input.split("\n\n").map { Pattern(it.split('\n')) }

    fun computeHorizontalReflection(): Int {
        for (i in 0..patterns.size){

        }
        return 0
    }
}

fun main() {}
