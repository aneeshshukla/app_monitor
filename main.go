package main

import (
	"embed"

	cmd "github.com/aneeshshukla/app_monitor/blob/main/docs/go_report"
)

var (
	//go:embed src/superfile_config/*
	content embed.FS
)

func main() {
	cmd.Run(content)
}
