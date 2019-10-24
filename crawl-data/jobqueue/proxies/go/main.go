package main

import (
	"time"

	"github.com/gocelery/gocelery"
	"github.com/gomodule/redigo/redis"
)

func main() {
	redisPool := &redis.Pool{
		Dial: func() (redis.Conn, error) {
			c, err := redis.DialURL("redis://h:iQwNeRiLAt8wTxM68JhrMY1Hftz2W8EQ@SG-celery-26745.servers.mongodirector.com:6379")
			if err != nil {
				return nil, err
			}
			return c, err
		},
	}

	cli, _ := gocelery.NewCeleryClient(
		gocelery.NewRedisBroker(redisPool),
		&gocelery.RedisCeleryBackend{Pool: redisPool},
		200, // number of workers
	)

	cli.Register("jobqueue.proxies.tasks.check_fresh_go", checkFresh)
	cli.StartWorker()
	time.Sleep(100 * time.Second)

	// stop workers gracefully (blocking call)
	// cli.StopWorker()
}
