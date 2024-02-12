package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
)

func load_input() string {
    content, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error reading file:", err)
    }
    str := string(content)
    return str
}

func part_one() int {
    str := load_input()
    sum := 0
    for i := 0; i < len(str)-1; i++ {
        if str[i] == str[i+1] {
            num, err := strconv.Atoi(string(str[i]))
            if err != nil {
                fmt.Println("Error converting string:", err)
            }
            sum += num
        }
    }
    if string(str[0]) == string(str[len(str)-1]) {
        num, err := strconv.Atoi(string(str[0]))
        if err != nil {
            fmt.Println("Error converting string:", err)
        }
        sum += num
    }
    return sum
}

func part_two() int {
    str := load_input()
    sum := 0
    half := len(str)/2
    for i := 0; i < half; i++ {
        if str[i] == str[i+half] {
            num, err := strconv.Atoi(string(str[i]))
            if err != nil {
                fmt.Println("Error converting string:", err)
            }
            sum += num
        }
    }
    return sum*2
}

func main() {
    num := part_one()
    num2 := part_two()
    fmt.Println(num)
    fmt.Println(num2)
}