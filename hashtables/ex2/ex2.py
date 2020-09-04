#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []

    # populate the cache with all tickets -> source : destination
    for i in range(length):
        cur_ticket = tickets[i]
        source = cur_ticket.source
        destination = cur_ticket.destination
        cache[source] = destination

    # set our starting destination , will always be NONE
    cur_dest = "NONE"

    # start loop for the length of the tickets arr
    # we dont need to add starting location to routes arr
    # set the next destination => add that destination to the router arr => change the cur dest to the one we just moved to
    for i in range(length):
        next_dest = cache[cur_dest]
        # print(next_dest)
        route.append(next_dest)
        cur_dest = next_dest

    print(f'cache: {cache}')
    print(f'Route: {route}')

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ ticket_2, ticket_1, ticket_3]

reconstruct_trip(tickets,3)

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")
#
tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


reconstruct_trip(tickets, 10)
'''
# One-Way Flight Trip

You've booked a _really_ cheap one-way flight. Unfortunately, that means
you have _tons_ of layovers before you reach your destination. The
morning of, you woke up late and had to scramble to the airport to catch
your first flight. However, in your rush, you accidentally scrambled all
your flight tickets. You don't know the route of your entire trip now!

Write a function `reconstruct_trip` to reconstruct your trip from your
mass of flight tickets. Each ticket is represented as a class with the
following form:

```
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
```

where the `source` string represents the starting airport and the
`destination` string represents the next airport along our trip. The
ticket for your first flight has a destination with a `source` of
`NONE`, and the ticket for your final flight has a `source` with a
`destination` of `NONE`. 

Pseudocode for an array of `Tickets` might look like this:

```
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
```

Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:

```
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
```

Your solution should run in linear time. You can assume that your
function will always be handed a valid ticket chain as input. 

## Hints

* The crux of this problem requires us to 'link' tickets together to
  reconstruct the entire trip. For example, if we have a ticket `('SJC',
  'BOS')` that has us flying from San Jose to Boston, then there exists
  another ticket where Boston is the starting location, `('BOS',
  'JFK')`. 

* We can hash each ticket such that the starting location is the key and
  the destination is the value. Then, when constructing the entire
  route, the `i`th location in the route can be found by checking the
  hash table for the `i-1`th location.


'''