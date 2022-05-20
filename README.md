# RLogic
This is the Repo for our KDD-2022 paper: *RLogic: Recurrent Logical Rule Learning from Knowledge Graphs*.

## Introduction
Logical rules are widely used to represent domain knowledge and hypothesis, which is fundamental to symbolic reasoning-based human intelligence. Very recently, it has been demonstrated that integrating logical rules into regular learning tasks can further enhance learning performance in a label-efficient manner. Many attempts have been made to learn logical rules automatically from knowledge graphs (KGs). However, a majority of existing methods entirely rely on observed rule instances to define the score function for rule evaluation and thus lack generalization ability and suffer from severe computational inefficiency. Instead of completely relying on rule instances for rule evaluation, RLogic defines a predicate representation learning-based scoring model, which is trained by sampled rule instances. In addition, RLogic incorporates one of the most significant properties of logical rules, the deductive nature, into rule learning, which is critical especially when a rule lacks supporting evidence. To push deductive reasoning deeper into rule learning, RLogic breaks a big sequential model into small atomic models in a recurrent way. Extensive experiments have demonstrated that RLogic is superior to existing state-of-the-art algorithms in terms of both efficiency and effectiveness.

## Model
<img src='./imgs/model.png' />


