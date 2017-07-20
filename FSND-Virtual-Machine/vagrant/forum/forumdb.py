# "Database code" for the DB Forum.

import psycopg2
import bleach

def get_posts():
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  cur.execute("SELECT time, content from posts ORDER BY time DESC")
  RESULTS = cur.fetchall()
  return RESULTS

def add_post(content):
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  cur.execute("INSERT INTO posts VALUES (%s)",
              (bleach.clean(content),))

  conn.commit()
  cur.close()
  conn.close()

  """Add a post to the 'database' with the current timestamp."""
  # POSTS.append((content, datetime.datetime.now()))


