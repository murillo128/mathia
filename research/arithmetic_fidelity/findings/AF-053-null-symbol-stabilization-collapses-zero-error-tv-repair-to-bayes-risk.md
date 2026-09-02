# AF-053 — Null-symbol stabilization collapses Blackwell-invariant TV zero-error repair to Bayes risk

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D,
\qquad
A=d(X),
\]

fix a strictly positive prior `\pi` on `X`, and let `K:X\rightsquigarrow Y` be a stochastic channel. For channels on a common finite output alphabet define

\[
\rho_\pi(K,L)
=
\sum_{x\in X}\pi_x\operatorname{TV}(K_x,L_x).
\]

For any finite output alphabet `Y'`, let `\mathcal Z_d^{(0)}(Y')` be the AF-011 zero-error faithful channels `X\rightsquigarrow Y'`: rows belonging to different discriminator classes have disjoint output supports.

Write `K'\sim_B K` when `K'` and `K` are Blackwell-equivalent experiments, i.e. each is obtainable from the other by a Markov post-processing kernel. Define the presentation-relaxed zero-error repair radius

\[
\mathfrak R_{\mathrm{BW}}(K;d,\pi)
=
\inf_{
\substack{
Y'\ \mathrm{finite},\\
K':X\rightsquigarrow Y',\ K'\sim_BK,\\
L\in\mathcal Z_d^{(0)}(Y')
}
}
\rho_\pi(K',L).
\]

Then

\[
\boxed{
\mathfrak R_{\mathrm{BW}}(K;d,\pi)=R_B(K),
}
\]

where `R_B(K)` is the Bayes error for predicting `d(X)` from one observation of `K` under prior `\pi`.

Moreover the infimum is attained after adjoining at most `|A|` **null output symbols**. Thus AF-047's additional Hall-coverage penalty is not merely sensitive to reversible cloning as in AF-052: once zero-probability output atoms are admitted as inessential presentation refinements, the entire excess structural repair cost disappears at a finite equivalent presentation.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{Blackwell-invariant TV distance to an unrestricted ambient-alphabet zero-error target}
=
\text{ordinary Bayes error after null stabilization}.}
\]

Therefore an ambient support-partition target carries quotient-invariant information beyond Bayes risk only if the available output atoms themselves are mathematically intrinsic, or if admissible repairs are required to descend through the declared presentation equivalence.

## Derivation

### Null-symbol stabilization is information-free

Choose a deterministic Bayes classifier

\[
\beta:Y\to A
\]

for the discriminator. Introduce one fresh symbol for every class,

\[
Y^+=Y\sqcup\{z_a:a\in A\},
\]

and extend `K` by zero mass:

\[
K^+(y\mid x)=K(y\mid x)\quad(y\in Y),
\qquad
K^+(z_a\mid x)=0.
\]

The inclusion channel `C:Y\rightsquigarrow Y^+` gives `K^+=CK`. Conversely, any deterministic merge that fixes every old output `y\in Y` and sends the null symbols arbitrarily back into `Y` satisfies `MK^+=K`. Hence

\[
K^+\sim_BK.
\]

No state-dependent side information has been added. On the embedded old simplex, total variation is also unchanged because all new coordinates are identically zero.

### The Bayes decoder gives an exact zero-error repair

For `x\in X` with class `a=d(x)`, define `L_x` by retaining precisely the outputs that the Bayes rule labels as `a` and moving all rejected mass to the private symbol `z_a`:

\[
L(y\mid x)
=
\begin{cases}
K(y\mid x),&\beta(y)=a,\\
0,&\beta(y)\ne a,
\end{cases}
\]

and

\[
L(z_a\mid x)
=
\sum_{\beta(y)\ne a}K(y\mid x),
\qquad
L(z_b\mid x)=0\quad(b\ne a).
\]

Every original output `y` is used only by rows whose class equals `\beta(y)`, while `z_a` is private to class `a`. Thus

\[
L\in\mathcal Z_d^{(0)}(Y^+).
\]

Put

\[
r_x=\sum_{\beta(y)\ne d(x)}K(y\mid x).
\]

Exactly `r_x` mass is removed from old coordinates and exactly `r_x` is added at `z_{d(x)}`, so

\[
\operatorname{TV}(K_x^+,L_x)=r_x.
\]

Consequently

\[
\rho_\pi(K^+,L)
=
\sum_x\pi_xr_x
=
\Pr_{\pi,K}[\beta(Y)\ne d(X)]
=R_B(K).
\]

This proves

\[
\mathfrak R_{\mathrm{BW}}(K;d,\pi)\le R_B(K)
\]

and shows that at most `|A|` null symbols suffice for attainment.

### Bayes risk is a universal lower bound

Now let `Y'` be any finite alphabet, let `K'\sim_BK`, and let

\[
L\in\mathcal Z_d^{(0)}(Y').
\]

Zero-error fidelity supplies a deterministic decoder

\[
\delta:Y'\to A
\]

that is correct `L`-almost surely. Let `P` and `Q` be the joint laws

\[
P(x,y')=\pi_xK'(y'\mid x),
\qquad
Q(x,y')=\pi_xL(y'\mid x).
\]

For the event

\[
E=\{(x,y'): \delta(y')=d(x)\}
\]

we have `Q(E)=1`. Since

\[
\operatorname{TV}(P,Q)=\rho_\pi(K',L),
\]

the defining event inequality for total variation gives

\[
P(E)\ge1-\rho_\pi(K',L).
\]

Thus `\delta` has classification error at most `\rho_\pi(K',L)` under `K'`, and therefore

\[
R_B(K')\le\rho_\pi(K',L).
\]

Blackwell-equivalent experiments have the same optimal risk for every fixed decision problem; applying the two garblings in opposite directions gives

\[
R_B(K')=R_B(K).
\]

Hence every admissible presentation and every zero-error repair satisfy

\[
R_B(K)\le\rho_\pi(K',L).
\]

Taking the infimum proves the reverse inequality and therefore the theorem.

## Exact controls

### AF-047's Hall penalty can disappear exactly without adding information

Take two discriminator classes with prior

\[
\pi_1=0.9,
\qquad
\pi_2=0.1,
\]

and identical channel rows

\[
K_1=K_2=\left(\frac12,\frac12\right).
\]

AF-047 gives, on the original two-output alphabet,

\[
R_B(K)=0.1,
\qquad
\operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)}(Y))=0.5.
\]

AF-052 shows that uniform `k`-fold output cloning keeps the experiment Blackwell-equivalent and TV-isometric but only yields

\[
0.1+\frac{0.4}{k}
\longrightarrow0.1.
\]

By contrast, adjoining the two null symbols `z_1,z_2` and using the construction above reaches

\[
\boxed{
\operatorname{dist}_{\rho_\pi}(K^+,\mathcal Z_d^{(0)}(Y^+))=0.1
}
\]

exactly at finite stabilization. The extra `0.4` was therefore entirely a feature of which output atoms the ambient target allowed a repair to occupy.

### A class need never be Bayes-optimal on an old output

The construction does not require every class to appear in the image of `\beta`. If a low-prior class is never Bayes-optimal on `Y`, all of its retained mass can be zero and its rejected mass is moved to its private null symbol. This is exactly the case in which the AF-047 Hall requirement is most visibly presentation-dependent.

## Prior art and novelty assessment

The surrounding ingredients are classical.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`, is the foundational source for equivalence of experiments through mutual randomization and equality of attainable decision risks.
- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/aoms/1177700372`, develops comparison/deficiency modulo Markov kernels and total-variation approximation.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), is a standard systematic treatment of randomizations, deficiencies, and their decision-risk interpretations.
- Claude E. Shannon, **“The Zero Error Capacity of a Noisy Channel,”** *IRE Transactions on Information Theory* 2(3), 8–19 (1956), DOI `10.1109/TIT.1956.1056798`, is the foundational source for zero-error support confusability.

No novelty is claimed for Blackwell equivalence, Bayes risk, total variation, adding null outcomes, or zero-error support separation. AF-047 and AF-052 already supply the fixed-presentation Hall formula and the reversible-cloning sensitivity. The durable result here is the exact synthesis needed for the Arithmetic Fidelity audit: **once null-symbol stabilization is included in the declared presentation equivalence, the quotient-invariant unrestricted zero-error TV repair radius is forced to equal Bayes error and cannot retain any additional Hall-style structural margin.**

## Boundary conditions and falsification checks

1. **Null outputs are the decisive admissibility assumption.** The theorem applies when adjoining zero-probability output symbols is considered an inessential representation change. If outputs are intrinsic physical, geometric, arithmetic, or operator objects, such stabilization may be forbidden and the conclusion need not apply.
2. **The target is unrestricted on the enlarged alphabet.** If the repair target is transported functorially from the original presentation, as in AF-052's descending target, private null symbols cannot be repurposed and the original distance is preserved instead.
3. **No information is hidden in the null symbols.** They have probability zero under `K^+` for every upstream state. A refinement carrying state-dependent positive-probability side information would not be a valid control.
4. **The result is decision-relative.** `R_B(K)` uses the fixed discriminator `d` and prior `\pi`; another discriminator or loss function defines another decision problem and another lower bound.
5. **Strict positivity of `\pi` is retained from AF-047.** It prevents nominal discriminator classes from being irrelevant solely because they have zero prior mass.
6. **The theorem does not say zero-error fidelity itself is equivalent to Bayes accuracy.** It classifies the infimal TV cost of repairing a Blackwell-equivalent presentation into an unrestricted zero-error channel.
7. **The same collapse is not automatic for another discrepancy.** The exact repair uses the identity `TV(P,Q)` = moved mass for this support projection. AF-049–AF-051 show that other divergences and quadratic geometries have different boundary behavior.

## Consequence for the line

AF-051 and AF-052 separated discrepancy geometry from target geometry under reversible refinements. AF-053 closes the most permissive finite-presentation version of that question:

\[
\boxed{
\text{if null alphabet stabilization is gauge, unrestricted support-partition repair has no intrinsic excess over Bayes risk.}
}
\]

This gives a sharper general gate for future Arithmetic Fidelity constructions. Whenever a proposed robustness or distance-to-faithfulness quantity is defined on a representation only up to reversible refinement, relabeling, basis splitting, or addition of null components, both the discrepancy **and the admissible target family** must descend to that equivalence. Otherwise the quantity can measure presentation capacity rather than survival of the intended discriminator.

For later prime/RH applications, the analogue is direct: if a supposedly structural margin can be reduced merely by adjoining mathematically null degrees of freedom and allowing the repair to occupy them, that margin is not evidence that prime-specific information survived the compression.