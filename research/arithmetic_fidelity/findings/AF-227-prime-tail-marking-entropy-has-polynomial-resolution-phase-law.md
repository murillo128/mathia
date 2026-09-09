# AF-227 — prime-tail marking entropy has a polynomial-resolution phase law

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `MARK-COMPLEXITY`, `CHROMATIC-ENTROPY`, `PRIME-TAIL`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-226 determines the exact **alphabet-cardinality** phase law for proximity markings on the rational-prime log-log source and deliberately leaves minimum marking entropy open. That entropy has a different, much slower phase scale.

For `Q>=3`, let

\[
S_Q:=\{-\log\log p:p\le Q,\ p\text{ prime}\},
\qquad
n_Q:=\pi(Q),
\tag{1}
\]

and let `P_Q` be uniform on the primes at most `Q`. For `r>0`, call a marking

\[
\lambda:S_Q\to A
\tag{2}
\]

`r`-proper when

\[
\lambda(s)=\lambda(t),\ s\ne t
\quad\Longrightarrow\quad
|s-t|>r.
\tag{3}
\]

Equivalently, `lambda` is a proper coloring of the proximity graph `G_r(S_Q)` from AF-224--AF-226. Define its minimum entropy, in natural logarithms, by

\[
E_Q(r)
:=
\inf_{\lambda\;r\text{-proper}}
H\!\left(\lambda(-\log\log P_Q)\right).
\tag{4}
\]

Put

\[
\beta_Q
:=
\frac{\log^+(1/r_Q)}{\log Q},
\qquad
\log^+x:=\max\{\log x,0\}.
\tag{5}
\]

If

\[
\beta_Q\longrightarrow\beta\in[0,\infty],
\tag{6}
\]

then

\[
\boxed{
\frac{E_Q(r_Q)}{\log\pi(Q)}
\longrightarrow
(1-\beta)_+,
}
\qquad
(1-\beta)_+:=\max\{1-\beta,0\}.
\tag{7}
\]

Thus the entropy cost has three regimes:

- if `log^+(1/r_Q)=o(log Q)`, then `E_Q(r_Q)~log pi(Q)`: every proper mark carries asymptotically full source entropy in logarithmic rate;
- if `r_Q=Q^{-\beta+o(1)}` with `0<beta<1`, then `E_Q(r_Q)~(1-beta) log pi(Q)`;
- if `r_Q<=Q^{-1+o(1)}` in the exponent sense `beta>=1`, then `E_Q(r_Q)=o(log pi(Q))`.

This phase law is genuinely different from AF-226. There the normalized minimum alphabet size is governed by `r_Q log Q`. Here the normalized minimum **entropy** is governed by `log(1/r_Q)/log Q`.

For example,

\[
r_Q=\frac1{(\log Q)^2}
\tag{8}
\]

satisfies `r_Q log Q->0`, so AF-226 gives

\[
K_Q(r_Q)=o(\pi(Q)).
\tag{9}
\]

Nevertheless `beta_Q->0`, and `(7)` gives

\[
\boxed{
E_Q(r_Q)\sim\log\pi(Q).
}
\tag{10}
\]

A vanishing fraction of the source cardinality can therefore suffice as the **number of available marks** while every valid marking still carries asymptotically the full prime identity in entropy rate. Alphabet fraction and information rate are distinct fidelity resources.

The theorem follows from a finite-`Q` sandwich that is useful independently. Put

\[
\ell_Q:=\log\log Q-\log\log2.
\tag{11}
\]

Then every `r>0` satisfies

\[
\boxed{
\left[
\log n_Q-
\log\!\left(1+\frac{\ell_Q}{r}\right)
\right]_+
\le
E_Q(r)
\le
\log\min\!\left\{
 n_Q,
 Qr\log Q+2
\right\}.
}
\tag{12}
\]

The lower bound is a source-packing bound: one mark class is an `r`-separated subset of a source interval of length only `O(log log Q)`. The upper bound uses AF-225's exact unit-interval coloring together with the elementary fact that a source `r`-window corresponds to a prime interval whose integer length is at most `Qr log Q`.

Consequently, if an AF-224 marked translation repair forces an `r_Q`-proper source mark and that mark is required to have entropy at most

\[
H(\lambda_Q)\le \rho\log\pi(Q)+o(\log Q),
\qquad 0\le\rho<1,
\tag{13}
\]

then every subsequential resolution exponent obeys

\[
\boxed{
\liminf_{Q\to\infty}
\frac{\log^+(1/r_Q)}{\log Q}
\ge 1-\rho.
}
\tag{14}
\]

In particular, **sub-source-rate entropy** requires polynomial deterioration of the AF-224 exclusion radius. Merely crossing below the `1/log Q` cardinality threshold from AF-226 is nowhere near enough.

## Derivation

### 1. Every color class has a packing-size bound

All points of `S_Q` lie in the interval

\[
[-\log\log Q,-\log\log2]
\tag{15}
\]

up to making the left endpoint slightly more negative than the actual largest prime below `Q`. Its length is `ell_Q` from `(11)`.

Fix an `r`-proper marking `lambda`. If one mark class contains

\[
s_1<s_2<\cdots<s_m,
\tag{16}
\]

then `(3)` gives

\[
s_{j+1}-s_j>r
\qquad(1\le j<m).
\tag{17}
\]

Therefore

\[
(m-1)r
<
s_m-s_1
\le\ell_Q,
\tag{18}
\]

so every mark class has cardinality at most

\[
m_Q(r)
:=
1+\left\lfloor\frac{\ell_Q}{r}\right\rfloor
\le
1+\frac{\ell_Q}{r}.
\tag{19}
\]

Because `P_Q` is uniform, every mark value has probability at most

\[
p_{\max}\le\frac{m_Q(r)}{n_Q}.
\tag{20}
\]

Shannon entropy dominates min-entropy:

\[
H(\lambda)
\ge
-\log p_{\max}.
\tag{21}
\]

Thus

\[
H(\lambda)
\ge
\log n_Q-\log m_Q(r)
\ge
\log n_Q-
\log\!\left(1+\frac{\ell_Q}{r}\right).
\tag{22}
\]

Taking the infimum over all proper markings and clipping the vacuous negative range at zero proves the lower half of `(12)`.

This bound does not use a clique, a decoder, or a Fano estimate. It prices the opposite combinatorial object: **how much source mass can be hidden inside one independent color class**. That is why it remains strong precisely in the shrinking-radius regime where AF-226's endpoint-clique entropy bound becomes weak.

### 2. Unit-interval coloring gives a matching entropy-rate upper bound

AF-225 proves that `G_r(S_Q)` is a unit interval graph and that

\[
K_Q(r)
:=
\chi(G_r(S_Q))
=
M_{S_Q}(r),
\tag{23}
\]

where `M_{S_Q}(r)` is the maximum number of source points in an interval of length `r`. Hence there exists an `r`-proper marking using exactly `K_Q(r)` marks. Its entropy is at most the logarithm of its alphabet size, so

\[
E_Q(r)
\le
\log K_Q(r).
\tag{24}
\]

Write

\[
a:=e^{-r}\in(0,1).
\tag{25}
\]

As in AF-226, a source interval of length `r` corresponds, after reversing the monotone coordinate, to a prime interval of the form

\[
[y^a,y].
\tag{26}
\]

For `y>=1`, the real interval length

\[
y-y^a
\tag{27}
\]

is increasing in `y`, because

\[
\frac{d}{dy}(y-y^a)
=1-a y^{a-1}
>0.
\tag{28}
\]

After truncating at `p<=Q`, any source `r`-window therefore contains at most

\[
Q-Q^a+2
\tag{29}
\]

integers, hence at most that many primes. The harmless `+2` absorbs endpoint conventions. Consequently

\[
K_Q(r)
\le
\min\{n_Q,Q-Q^a+2\}.
\tag{30}
\]

Now

\[
\begin{aligned}
Q-Q^a
&=Q\left(1-e^{-(1-a)\log Q}\right)\\
&\le Q(1-a)\log Q\\
&=Q(1-e^{-r})\log Q\\
&\le Qr\log Q.
\end{aligned}
\tag{31}
\]

Combining `(24)`, `(30)`, and `(31)` proves the upper half of `(12)`.

No short-interval prime theorem is used. The upper bound deliberately counts **integers** rather than trying to estimate primes in a very short moving interval. That coarse count is already sharp enough on logarithmic entropy scale.

### 3. The two finite-`Q` bounds have the same exponent

The prime number theorem gives

\[
\log n_Q
=
\log\pi(Q)
=
\log Q+o(\log Q).
\tag{32}
\]

Also

\[
\ell_Q=O(\log\log Q),
\qquad
\log(1+\ell_Q)=o(\log Q).
\tag{33}
\]

Suppose first that `0<=beta<1`. If `beta=0`, then

\[
\log^+(1/r_Q)=o(\log Q),
\tag{34}
\]

and `(22)` immediately gives

\[
\frac{E_Q(r_Q)}{\log n_Q}\ge1-o(1),
\tag{35}
\]

while the trivial entropy bound `E_Q<=log n_Q` gives the reverse inequality.

If `0<beta<1`, eventually `r_Q<1` and

\[
\log\!\left(1+\frac{\ell_Q}{r_Q}\right)
=
\log(1/r_Q)+o(\log Q)
=
\beta\log Q+o(\log Q).
\tag{36}
\]

The lower half of `(12)` therefore gives

\[
\liminf
\frac{E_Q(r_Q)}{\log n_Q}
\ge1-\beta.
\tag{37}
\]

On the other hand,

\[
Qr_Q\log Q
=
\exp\!\left((1-\beta+o(1))\log Q\right),
\tag{38}
\]

so the upper half of `(12)` gives

\[
\limsup
\frac{E_Q(r_Q)}{\log n_Q}
\le1-\beta.
\tag{39}
\]

This proves `(7)` for `beta<1`.

If `beta=1`, then

\[
\log(Qr_Q\log Q+2)=o(\log Q),
\tag{40}
\]

and the upper half of `(12)` gives

\[
E_Q(r_Q)=o(\log n_Q).
\tag{41}
\]

The same conclusion is immediate for every `beta>1` and for `beta=infinity`. Since entropy is nonnegative, `(7)` follows in all remaining regimes.

### 4. Entropy compression forces polynomial resolution collapse

Let an actual marking obey `(13)`. If `(14)` failed, there would be an `epsilon>0` and a subsequence along which

\[
\frac{\log^+(1/r_Q)}{\log Q}
\le1-\rho-\epsilon.
\tag{42}
\]

Passing to a further subsequence if necessary, the left side converges to some

\[
\beta\le1-\rho-\epsilon.
\tag{43}
\]

Equation `(7)` would force every proper marking on that subsequence to satisfy

\[
\frac{H(\lambda_Q)}{\log\pi(Q)}
\ge
1-\beta-o(1)
\ge
\rho+\epsilon-o(1),
\tag{44}
\]

contradicting `(13)`. This proves `(14)`.

When AF-224 supplies the exclusion radius through a local sample-coordinate Lipschitz bound, this has a direct representation-theoretic reading. Using AF-226's notation, if

\[
\Omega_{0,Q}(r)\le \mathcal L_Q r,
\qquad
\Delta_Q:=c_{*,Q}-\eta_Q>0,
\tag{45}
\]

then the conservative choice

\[
r_Q=\frac{\Delta_Q}{2\mathcal L_Q}
\tag{46}
\]

forces a proper mark whenever that radius lies in the declared local scale. A mark of entropy fraction at most `rho<1` can therefore survive only if

\[
\boxed{
\liminf_{Q\to\infty}
\frac{
\log^+\!\left(2\mathcal L_Q/\Delta_Q\right)
}{\log Q}
\ge1-\rho.
}
\tag{47}
\]

Thus expected-information compression is much more demanding than merely reducing mark cardinality below `pi(Q)`. To save a fixed positive fraction of source entropy, the separation-to-continuity ratio must deteriorate by a corresponding **power of `Q`**.

## Exact controls and boundaries

### This is chromatic entropy, not graph entropy

The quantity `(4)` is the minimum entropy of a proper coloring under the declared uniform vertex law, usually called **chromatic entropy**. It is not Körner's graph entropy, although the two are classically related. The distinction matters because minimum-entropy coloring is a genuine optimization problem even when the chromatic number is known.

### The uniform prime cutoff is load bearing

The source law in `(4)` is uniform on primes at most `Q`. Under a deliberately nonuniform law, a large independent color class can carry much more probability mass than its cardinality suggests, and the entropy phase curve can change. AF-227 therefore does not claim a distribution-free expected-bit lower bound.

### The theorem identifies an entropy rate, not an additive asymptotic

Equation `(7)` determines the coefficient of `log pi(Q)`. It does not determine the additive `O(log log Q)` or smaller terms, nor the exact entropy-minimizing coloring. The elementary sandwich `(12)` is intentionally too coarse for those finer questions.

### Proper coloring remains only a necessary analytic resource

As in AF-225--AF-226, a proper proximity coloring does not construct the analytic maps `Phi`, `Psi`, or mark-specific decoders of AF-224. The upper bound in `(12)` proves only that a combinatorial marking with that entropy scale exists. A full marked translation representation may require strictly more side information.

### The phase scale is coordinate specific

The source span and window geometry come from `v_p=-log log p`. A different source coordinate changes both `ell_Q` and the relation between an `r`-window and the prime variable. The polynomial scale in `(7)` is therefore not a universal arithmetic coding law.

### Near-full source identity is still not rational-prime specificity

Even a mark with entropy asymptotic to `log pi(Q)` may encode only source identity and no canonical arithmetic invariant. AF-227 prices one repair resource; it does not show that retaining that resource helps any later RH-relevant compression.

## Prior art and novelty assessment

The entropy-coloring problem is classical. Noga Alon and Alon Orlitsky, **“Source Coding and Graph Entropies,”** *IEEE Transactions on Information Theory* **42**(5), 1329--1339 (1996), DOI `10.1109/18.532875`, introduced the chromatic-entropy connection to one-shot source coding with side information. Jean Cardinal, Samuel Fiorini, and Gwenaël Joret, **“Minimum Entropy Coloring,”** *Journal of Combinatorial Optimization* **16**(4), 361--377 (2008), DOI `10.1007/s10878-008-9152-2`, studies the minimum-entropy coloring problem computationally and proves NP-hardness even for interval graphs. H. S. Witsenhausen, **“The Zero-Error Side Information Problem and Chromatic Numbers,”** *IEEE Transactions on Information Theory* **22**(5), 592--593 (1976), DOI `10.1109/TIT.1976.1055607`, is the classical zero-error coloring precursor used already in AF-224--AF-226.

The graph structure is also classical: the proximity graph of one-dimensional points is a unit interval graph, and the equality of chromatic number with maximum clique size is a standard interval-graph fact. The arithmetic asymptotic uses only the prime number theorem through `log pi(Q)~log Q`; the matching upper bound at very small radii uses only integer counting.

The inequalities behind `(12)` are elementary consequences of independent-set packing, Shannon entropy being at least min-entropy, and the existence of a proper interval-graph coloring. A targeted literature search found the established chromatic-entropy and interval-graph frameworks but did not locate the specific transformed-prime asymptotic `(7)`. **No novelty claim is made from that absence.** The durable Arithmetic Fidelity content is the category-specific synthesis: once AF-224 turns a translation repair into a proximity-coloring requirement, prime-tail source geometry separates cardinality complexity and entropy complexity into two different resolution scales.

## Consequence for the research line

AF-226 leaves an apparent escape: once `r_Q=o(1/log Q)`, the minimum mark alphabet is `o(pi(Q))`. AF-227 shows that this can be deeply misleading if the intended side-information resource is expected information rather than raw alphabet cardinality. Every subpolynomially shrinking radius—including polylogarithmic shrinkage—still costs asymptotically the full `log pi(Q)` source entropy.

To reduce the mark entropy by a fixed fraction, a translation-category repair must drive its confusability radius down at a **polynomial** rate in `Q`, equivalently pay a polynomial loss in separation margin, sample-coordinate conditioning, approximation/inverse resolution, or another resource entering the AF-224 radius. The remaining marked-translation escape is therefore no longer merely “let the alphabet grow”: it must state whether it is paying cardinality, entropy, conditioning, or geometry, because those resources have quantitatively different phase laws.