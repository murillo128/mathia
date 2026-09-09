# AF-230 — stochastic excess-error localization has the same prime-tail rate-distortion phase

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-THEOREM-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `RATE-DISTORTION`, `STOCHASTIC`, `PRIME-TAIL`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-228 derives the deterministic one-shot entropy price of localizing the rational-prime log-log source with a nonzero failure budget, while AF-229 closes the stochastic relaxation only at zero error. The remaining stochastic/nonzero-error boundary has the same first-order phase law and is exactly a classical rate-distortion problem with a threshold distortion.

For `Q>=3`, let

\[
S_Q:=\{-\log\log p:p\le Q,\ p\text{ prime}\},
\qquad
n_Q:=\pi(Q),
\tag{1}
\]

and let `X_Q` be uniform on `S_Q`. For `r>0` and `0<=\delta<1`, define the stochastic localization information

\[
\mathcal R_Q(r,\delta)
:=
\inf I(X_Q;M),
\tag{2}
\]

where the infimum is over arbitrary finite-valued stochastic marks `P_{M\mid X_Q}` and decoders `d` satisfying

\[
\Pr\{|X_Q-d(M)|>r\}\le\delta.
\tag{3}
\]

Equivalently, with the binary threshold distortion

\[
\rho_r(x,\hat x):=\mathbf 1_{\{|x-\hat x|>r\}},
\tag{4}
\]

`\mathcal R_Q(r,\delta)` is exactly the Shannon single-letter rate-distortion function of the finite source `X_Q` at distortion level `\delta`:

\[
\boxed{
\mathcal R_Q(r,\delta)
=
\inf_{P_{\widehat X\mid X_Q}:\;\mathbb E\rho_r(X_Q,\widehat X)\le\delta}
I(X_Q;\widehat X).
}
\tag{5}
\]

Let

\[
N_Q(t):=
\max_{x\in\mathbb R}
\#\bigl(S_Q\cap[x,x+t]\bigr)
\tag{6}
\]

be the local occupancy. Then every stochastic localization channel obeys the finite converse

\[
\boxed{
\mathcal R_Q(r,\delta)
\ge
\left[
(1-\delta)
\bigl(\log n_Q-\log N_Q(2r)\bigr)
-\log2
\right]_+.
}
\tag{7}
\]

AF-228's deterministic quantizer is an admissible stochastic channel, so if

\[
m_Q:=\lfloor\delta n_Q\rfloor,
\qquad
\delta_Q^*:=\frac{m_Q}{n_Q},
\tag{8}
\]

\[
\ell_Q:=\log\log Q-\log\log2,
\qquad
J_Q(r,\delta)
:=
\min\!\left\{
 n_Q-m_Q,
 \left\lceil\frac{\ell_Q}{2r}\right\rceil
\right\},
\tag{9}
\]

then

\[
\boxed{
\mathcal R_Q(r,\delta)
\le
h(\delta_Q^*)
+(1-\delta_Q^*)\log J_Q(r,\delta),
}
\tag{10}
\]

where `h(u)=-u\log u-(1-u)\log(1-u)`.

Consequently, for sequences `r_Q>0` and `\delta_Q\to\delta` with `0<=\delta<1`, put

\[
\beta_Q
:=
\frac{\log^+(1/r_Q)}{\log Q}.
\tag{11}
\]

If

\[
\beta_Q\longrightarrow\beta\in[0,\infty],
\tag{12}
\]

then

\[
\boxed{
\frac{\mathcal R_Q(r_Q,\delta_Q)}{\log\pi(Q)}
\longrightarrow
(1-\delta)\min\{\beta,1\}.
}
\tag{13}
\]

Thus arbitrary stochastic marking does not improve the **first-order** information price found by AF-228. If `R_Q(r,\delta)` denotes AF-228's deterministic minimum mark entropy, then along every regime in `(11)`--`(12)`,

\[
\boxed{
\frac{R_Q(r_Q,\delta_Q)-\mathcal R_Q(r_Q,\delta_Q)}
{\log\pi(Q)}
\longrightarrow0.
}
\tag{14}
\]

Randomization may change finite additive terms, but it cannot change the logarithmic prime-tail localization phase while the distortion criterion remains `(4)`.

## Derivation

### 1. The stochastic mark problem reduces exactly to a reproduction channel

Given any admissible stochastic mark `M` and decoder `d`, set

\[
\widehat X:=d(M).
\tag{15}
\]

Then `X_Q -> M -> \widehat X` is a Markov chain, so data processing gives

\[
I(X_Q;\widehat X)\le I(X_Q;M),
\tag{16}
\]

and `(3)` is exactly

\[
\mathbb E\rho_r(X_Q,\widehat X)\le\delta.
\tag{17}
\]

Therefore the right-hand side of `(5)` is no larger than `\mathcal R_Q(r,\delta)`.

Conversely, for any reproduction channel `P_{\widehat X\mid X_Q}` satisfying `(17)`, take `M=\widehat X` and decode by the identity map. This is admissible in `(2)` and has the same mutual information. Hence equality holds in `(5)`.

This identification is classical rate-distortion mathematics. The line-specific content begins with the exact geometry of the prime-tail source and the resulting phase `(13)`.

### 2. A Fano-type occupancy converse survives arbitrary stochasticization

Fix an admissible `M,d` and define the failure indicator

\[
F:=\mathbf 1_{\{|X_Q-d(M)|>r\}},
\qquad
\theta:=\Pr(F=1)\le\delta.
\tag{18}
\]

For each realized mark `m`, conditional on success every possible value of `X_Q` lies in

\[
[d(m)-r,d(m)+r],
\tag{19}
\]

which contains at most `N_Q(2r)` source points. Hence

\[
H(X_Q\mid M,F=0)\le\log N_Q(2r).
\tag{20}
\]

On failure, trivially

\[
H(X_Q\mid M,F=1)\le\log n_Q.
\tag{21}
\]

Conditioning on `F` gives

\[
H(X_Q\mid M)
\le
h(\theta)
+(1-\theta)\log N_Q(2r)
+\theta\log n_Q.
\tag{22}
\]

Since `H(X_Q)=\log n_Q`,

\[
I(X_Q;M)
\ge
(1-\theta)
\bigl(\log n_Q-\log N_Q(2r)\bigr)
-h(\theta).
\tag{23}
\]

Using `\theta\le\delta`, `h(\theta)\le\log2`, and `N_Q(2r)\le n_Q` proves `(7)`.

Crucially, no determinism of the encoder was used. The lower bound prices the posterior uncertainty remaining after an arbitrary channel, not the alphabet entropy of a deterministic mark.

### 3. Deterministic quantization remains a valid stochastic achievability bound

AF-228 constructs a deterministic mark which discards `m_Q` source points into one failure class and partitions the remaining source span into intervals of diameter at most `2r`. Its mark entropy is bounded by the right-hand side of `(10)`.

A deterministic encoder is a special stochastic channel and for it

\[
I(X_Q;M)=H(M).
\tag{24}
\]

Therefore the same construction proves `(10)` without any new coding argument.

The stochastic optimum can be smaller at finite `Q`; `(10)` is only an achievability bound. The point is that `(7)` and `(10)` already agree to first order on the prime-tail scaling regimes.

### 4. Prime-tail geometry forces the same phase as the deterministic problem

AF-228 establishes the elementary occupancy estimate

\[
N_Q(2r)
\le
\min\{n_Q,\,2Qr\log Q+2\},
\tag{25}
\]

and uses only the prime number theorem at logarithmic scale,

\[
\log n_Q
=
\log\pi(Q)
=
\log Q+o(\log Q),
\tag{26}
\]

while

\[
\ell_Q=O(\log\log Q).
\tag{27}
\]

If `0<\beta<1`, `(25)` gives

\[
\log N_Q(2r_Q)
\le
(1-\beta)\log Q+o(\log Q),
\tag{28}
\]

so `(7)` yields

\[
\liminf
\frac{\mathcal R_Q(r_Q,\delta_Q)}{\log n_Q}
\ge
(1-\delta)\beta.
\tag{29}
\]

Equation `(10)` gives the matching upper bound because

\[
\log J_Q(r_Q,\delta_Q)
\le
\beta\log Q+o(\log Q).
\tag{30}
\]

For `\beta=0`, the interval cover has `\exp(o(\log Q))` cells, so `(10)` gives `\mathcal R_Q=o(\log n_Q)`. For `\beta>=1`, `(25)` makes the occupancy contribution negligible at logarithmic scale while the cap `J_Q\le n_Q-m_Q` gives the matching coefficient `1-\delta`. This proves `(13)`.

AF-228 proves the identical normalized limit for `R_Q`. Since

\[
0\le\mathcal R_Q(r,\delta)\le R_Q(r,\delta),
\tag{31}
\]

the equality of their normalized limits proves `(14)`.

## Exact controls and boundaries

### The rate-distortion identification is classical

Equation `(5)` is not a new information-theory theorem. Shannon's fidelity-criterion framework defines rate-distortion through mutual-information minimization under an expected distortion constraint. Here the excess-localization event becomes an ordinary binary distortion by choosing `(4)`.

The source-specific statement is that the prime-tail occupancy and covering geometry make this classical stochastic relaxation inherit exactly the deterministic first-order phase found in AF-228.

### This is an information price, not a finite-code operational rate

`\mathcal R_Q` is a single-letter mutual-information infimum. It is not the minimum number of bits in a particular one-shot fixed-length code and does not assert an asymptotic block-coding theorem for repeated prime samples.

Finite-blocklength lossy source coding with excess-distortion probability has a richer operational theory. Kostina--Verdú derive general finite-blocklength achievability and converse bounds for that problem. The present result uses only the elementary mutual-information/Fano side needed for the Mathia source geometry.

### Randomization is closed only at first order for nonzero error

Equation `(14)` says that stochasticization cannot improve the leading `\log\pi(Q)` coefficient. It does **not** say

\[
\mathcal R_Q(r,\delta)=R_Q(r,\delta)
\tag{32}
\]

at finite `Q`. Fractional stochastic allocation of the error budget can alter additive or lower-order terms, and no exact finite equality is claimed.

At `\delta=0`, AF-229 gives a sharper exact graph-entropy description. With radius normalization, zero-error localization is complement graph entropy because the prime-tail proximity graph is a unit interval graph. Positive error destroys the posterior-support condition used by that exact complement identity, so `(5)` rather than perfect-graph entropy is the correct general stochastic framework.

### The phase law is not a rational-prime discriminator

The converse `(7)` holds for any finite one-dimensional source after replacing `N_Q` by its local occupancy. The matching upper construction depends only on source span and covering. Therefore a matched non-prime point set with the same occupancy/covering exponents can reproduce the same information phase.

The rational primes enter `(13)` through the specific source cardinality and elementary prime-tail occupancy estimate. The phase law prices what localization must retain; it does not by itself prove that the retained information is uniquely arithmetic or useful for RH.

### The uniform cutoff law remains load bearing for coefficient `1-delta`

As in AF-228, the explicit coefficient `(1-\delta)` uses the uniform distribution on primes up to `Q`. For a nonuniform source law, the correct rate-distortion function still exists and `(5)` remains exact, but the simple cardinality/occupancy entropy calculation need not give the same normalized phase.

## Prior art and novelty assessment

Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record*, vol. 7, 1959, pp. 142–163, introduced the fidelity/rate-distortion framework in which a source is reproduced through a distortion measure and the relevant information quantity is optimized under a distortion constraint. IEEE record: https://ieeexplore.ieee.org/document/5311476

Victoria Kostina and Sergio Verdú, **“Fixed-Length Lossy Compression in the Finite Blocklength Regime,”** *IEEE Transactions on Information Theory* 58(6), 2012, pp. 3309–3338, DOI `10.1109/TIT.2012.2186786`, derive tight general achievability and converse bounds for lossy source coding at finite blocklength with a prescribed probability that distortion exceeds a threshold. Author repository: https://authors.library.caltech.edu/records/azxwc-3dx27 ; preprint: https://arxiv.org/abs/1102.3944

The entropy decomposition in `(22)`--`(23)` is a Fano-type one-shot converse and is classical in mechanism. No novelty is claimed for Shannon rate-distortion theory, data processing, Fano-style conditioning, or finite-blocklength excess-distortion coding.

The Mathia-specific contribution is the exact specialization to the AF prime-tail geometry and the conclusion that **the stochastic Shannon relaxation and the deterministic marking problem have the same first-order localization-fidelity phase across every polynomial resolution regime**. This closes the explicit nonzero-error stochastic boundary left between AF-228 and AF-229 without upgrading a classical information-theory mechanism into a novel theorem claim.

## Research consequence

AF-228 and AF-229 together left two possible randomization escape routes: zero-error stochastic marking and positive-error stochastic localization. AF-229 closes the first exactly through perfect-graph entropy; this finding closes the second at first order through rate-distortion.

Within the prime-tail localization model, changing the encoder from deterministic to stochastic is therefore no longer a plausible way to reduce the leading repair cost. A genuinely cheaper route must instead change at least one load-bearing ingredient: the distortion notion, the source law, the retained geometry, the allowed ambiguity structure, or the information objective itself.
