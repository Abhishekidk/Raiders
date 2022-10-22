model = Sequential()
model.add(Dense(128,input_shape=(len(train_x[0]),), activation="relu"))
model.add(dropout(0.5))
model.add(Dense(64,activation="relu"))
model.add(dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

sgd=SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical crossentropy", optimizer=sgd, meterics=["accuracy"])

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_siza=5, verbose=1)
model.save("chatbot model.model")
Print("Trained")
