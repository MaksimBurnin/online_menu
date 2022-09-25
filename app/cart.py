class Cart:
    def __init__(self, session):
        self.session = session
        items = session.get('cart', {})
        # Making sure the list keys are int
        self.items = { int(k) : v for k,v in items.items()}

    def save(self):
        self.session['cart'] = self.items
        print(self.items)

    def add(self, pk):
        pk = int(pk)
        if pk not in self.items.keys():
            self.items[pk] = 0

        self.items[pk] += 1

        self.save()

    def remove(self, pk):
        pk = int(pk)
        if pk not in self.items.keys():
            return

        self.items[pk] -= 1

        if self.items[pk] <= 0:
            self.items.pop(pk)

        self.save();

    @property
    def item_pks(self):
        return self.items.keys()
