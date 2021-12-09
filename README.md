# load-shedding-api
This is the RESTful API for automating an optimum Load Shedding mechanism.

## Database Structure

Built based on Apache Cassandra.

### Queries
- Get device by customer
- Get device data values by device
- Get total consumption by customer
- Get total consumption by device by date
- Get total consumption by area
- Get customers by priority index
- Get customers by users
- Get customers by area
- Get customers by status
- Get admins by user
- Get ceb users by users
- Get load shedding by area by status

### Tables
- device
  * partition key: customer ID
  * cluster key: date
- device data
  * partition key: device ID
  * cluster key: timestamp
- customer consumption
  * partition key: customer ID
  * cluster key: date
- device consumption
  * partition key: device ID, date
  * cluster key: date
- area consumption
  * partition key: area ID
  * cluster key: timestamp
- customer priorities
  * partition key: priority index
- customer areas
  * partition key: area ID
- customer statuses
  * partition key: status
- users
  * partition key: ID
- admins
  * partition key: email
- ceb_users
  * partition key: email
- customers
  * partition key: email
- areas
  * partition key: status
- load sheddings
  * partition key: area
  * cluster key: timestamp

