# AF-228 — prime-tail localization entropy complements proximity separation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `RATE-DISTORTION`, `PRIME-TAIL`, `PHASE-LAW`, `CHROMATIC-ENTROPY`, `COMPLEMENT-DUALITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-227 prices the entropy needed to keep **nearby source points separated** under an `r`-proper mark. The complementary question is how much entropy is needed to say **where the source point is**, up to a declared localization error.

For `Q>=3`, let

\[
S_Q:=\{-\log\log p:p\le Q,\ p\text{ prime}\},
\qquad
n_Q:=\pi(Q),
\tag{1}
\]

and let `X_Q` be uniform on `S_Q`. For `r>0` and `0<=delta<1`, define the deterministic localization entropy

\[
R_Q(r,\delta)
:=
\inf H(M),
\tag{2}
\]

where the infimum is over deterministic marks `M=lambda(X_Q)` and decoders `d` satisfying

\[
\Pr\{|X_Q-d(M)|>r\}\le\delta.
\tag{3}
\]

All logarithms are natural. Define also the local occupancy

\[
N_Q(t)
:=
\max_{x\in\mathbb R}
\#\bigl(S_Q\cap[x,x+t]\bigr)
\tag{4}
\]

and the source span

\[
\ell_Q:=\log\log Q-\log\log2.
\tag{5}
\]

Then `R_Q` obeys the finite-`Q` sandwich

\[
\boxed{
\left[
(1-\delta)
\bigl(\log n_Q-\log N_Q(2r)\bigr)
-\log2
\right]_+
\le
R_Q(r,\delta)
}
\tag{6}
\]

and, writing

\[
m_Q:=\lfloor\delta n_Q\rfloor,
\qquad
\delta_Q^*:=\frac{m_Q}{n_Q},
\qquad
J_Q(r,\delta)
:=
\min\!\left\{
 n_Q-m_Q,
 \left\lceil\frac{\ell_Q}{2r}\right\rceil
\right\},
\tag{7}
\]

also

\[
\boxed{
R_Q(r,\delta)
\le
h(\delta_Q^*)
+(1-\delta_Q^*)\log J_Q(r,\delta),
}
\tag{8}
\]

where `h(u)=-u log u-(1-u)log(1-u)` is binary entropy.

The prime-tail coordinate supplies the elementary occupancy bound

\[
N_Q(2r)
\le
\min\{n_Q,\,2Qr\log Q+2\}.
\tag{9}
\]

Consequently, for sequences `r_Q>0`, `delta_Q->delta` with `0<=delta<1`, put

\[
\beta_Q
:=
\frac{\log^+(1/r_Q)}{\log Q}.
\tag{10}
\]

If

\[
\beta_Q\longrightarrow\beta\in[0,\infty],
\tag{11}
\]

then

\[
\boxed{
\frac{R_Q(r_Q,\delta_Q)}{\log\pi(Q)}
\longrightarrow
(1-\delta)\min\{\beta,1\}.
}
\tag{12}
\]

Thus localization has the phase curve complementary to AF-227's proximity-separation entropy:

- subpolynomially shrinking resolution costs `o(log pi(Q))` localization entropy;
- if `r_Q=Q^{-\beta+o(1)}` with `0<beta<1`, localization costs `(1-delta) beta log pi(Q)` to first order;
- once `beta>=1`, zero-error localization costs asymptotically the full `log pi(Q)` source identity, while allowed error fraction `delta` reduces that first-order cost to `(1-delta) log pi(Q)`.

There is also an exact zero-error graph complement relation. Let `G_r(S_Q)` be the AF-224--AF-227 proximity graph, with an edge when two distinct source points have distance at most `r`. Then

\[
R_Q(r/2,0)
=
\text{minimum chromatic entropy of }\overline{G_r(S_Q)}.
\tag{13}
\]

If `E_Q(r)` is AF-227's minimum entropy of a proper coloring of `G_r(S_Q)`, then for every finite `Q` and every `r>0`,

\[
\boxed{
E_Q(r)+R_Q(r/2,0)\ge\log n_Q.
}
\tag{14}
\]

Combining AF-227 with `(12)` shows that this lower bound is asymptotically saturated on every polynomial resolution scale:

\[
\boxed{
E_Q(r_Q)+R_Q(r_Q/2,0)
=
\log\pi(Q)+o(\log Q).
}
\tag{15}
\]

For `0<beta<1`, the full prime-source identity entropy therefore splits to first order into a proximity-separation fraction `1-beta` and a localization fraction `beta`.

## Derivation

### 1. A localization mark cannot hide too many successful source points

Fix an admissible deterministic mark `M=lambda(X_Q)` and decoder `d`. Let

\[
F:=\mathbf 1_{\{|X_Q-d(M)|>r\}},
\qquad
\theta:=\Pr(F=1)\le\delta.
\tag{16}
\]

For a fixed mark value `m`, every successful source point with that mark lies in

\[
[d(m)-r,d(m)+r],
\tag{17}
\]

an interval of length `2r`. Hence at most `N_Q(2r)` successful source values can occur for one mark.

Conditioning first on `F` gives

\[
\begin{aligned}
H(X_Q\mid M)
&\le
H(F\mid M)
+\Pr(F=0)H(X_Q\mid M,F=0)
+\Pr(F=1)H(X_Q\mid M,F=1)\\
&\le
h(\theta)
+(1-\theta)\log N_Q(2r)
+\theta\log n_Q.
\end{aligned}
\tag{18}
\]

Because `M` is a deterministic function of the uniform source,

\[
H(M)=H(X_Q)-H(X_Q\mid M)
=\log n_Q-H(X_Q\mid M).
\tag{19}
\]

Therefore

\[
H(M)
\ge
(1-\theta)
\bigl(\log n_Q-\log N_Q(2r)\bigr)
-h(\theta).
\tag{20}
\]

Using `theta<=delta`, `h(theta)<=log2`, and the nonnegativity of the parenthesized term proves `(6)`.

This is a one-shot excess-distortion counting bound. It does not assume independent repeated samples, an asymptotic coding theorem, or a probabilistic model for primes beyond the declared uniform cutoff law.

### 2. Interval quantization gives the matching upper exponent

Choose any `m_Q=floor(delta n_Q)` source points and permit them to fail. Give all of those points one common failure mark. The remaining source points still lie in an interval of length at most `ell_Q`.

Partition that interval into

\[
\left\lceil\frac{\ell_Q}{2r}\right\rceil
\tag{21}
\]

subintervals of diameter at most `2r`, ignoring empty cells. Give each nonempty successful cell one mark and decode it to the cell midpoint. Every successful point is then reconstructed within distance `r`. There are at most `J_Q(r,delta)` nonempty successful marks.

The failure mark has probability `delta_Q^*`; conditional on success, entropy is at most `log J_Q`. Hence

\[
H(M)
\le
h(\delta_Q^*)
+(1-\delta_Q^*)\log J_Q(r,\delta),
\tag{22}
\]

which proves `(8)`.

The construction is intentionally crude. It does not optimize cell placement or the identity of discarded source points. Those refinements can change additive terms but not the logarithmic phase derived below.

### 3. Prime-tail occupancy has the required exponent

AF-227 already establishes the elementary window conversion used here. A source interval of length `t` corresponds, after reversing the monotone coordinate, to a prime interval of the form

\[
[y^{e^{-t}},y].
\tag{23}
\]

After truncating at `p<=Q`, its number of source points is at most its number of integers, so

\[
N_Q(t)
\le
\min\{n_Q,Q-Q^{e^{-t}}+2\}
\le
\min\{n_Q,Qt\log Q+2\}.
\tag{24}
\]

Putting `t=2r` gives `(9)`. No short-interval prime theorem is used.

The prime number theorem is needed only at logarithmic scale:

\[
\log n_Q
=
\log\pi(Q)
=
\log Q+o(\log Q),
\tag{25}
\]

while

\[
\ell_Q=O(\log\log Q).
\tag{26}
\]

### 4. Localization entropy has phase `(1-delta) min{beta,1}`

Suppose first that `0<beta<1`. Equations `(9)`--`(11)` imply

\[
\log N_Q(2r_Q)
\le
(1-\beta)\log Q+o(\log Q),
\tag{27}
\]

so `(6)` yields

\[
\liminf
\frac{R_Q(r_Q,\delta_Q)}{\log n_Q}
\ge
(1-\delta)\beta.
\tag{28}
\]

On the other hand,

\[
\log J_Q(r_Q,\delta_Q)
\le
\beta\log Q+o(\log Q),
\tag{29}
\]

and `delta_Q^*=delta_Q+o(1)`, so `(8)` gives the matching upper bound.

If `beta=0`, the interval cover in `(8)` has only `exp(o(log Q))` cells, hence

\[
R_Q(r_Q,\delta_Q)=o(\log n_Q).
\tag{30}
\]

If `beta>=1`, `(9)` gives

\[
\log N_Q(2r_Q)=o(\log Q)
\tag{31}
\]

in the exponent sense at `beta=1` and beyond, while the cap `J_Q<=n_Q-m_Q` gives

\[
\limsup
\frac{R_Q(r_Q,\delta_Q)}{\log n_Q}
\le1-\delta.
\tag{32}
\]

The lower bound `(6)` gives the reverse inequality. This proves `(12)` in every regime, including `beta=infinity`.

### 5. Zero-error localization is complement coloring

A zero-error radius-`r/2` localization mark groups together only source points that can share one decoder output while staying within distance `r/2`. For a subset of the real line this is equivalent to saying that the class has diameter at most `r`.

Thus every localization class is a clique of `G_r(S_Q)`, equivalently an independent set of the complement graph. Conversely, every such clique can be decoded to the midpoint of its extreme points. Therefore zero-error localization markings at radius `r/2` are exactly proper colorings of `overline{G_r(S_Q)}`, proving `(13)`.

Now let `C` be any proper coloring of `G_r(S_Q)` and `D` any proper coloring of its complement. Two distinct vertices are adjacent in exactly one of these two graphs, so they cannot share both colors. The pair `(C,D)` therefore identifies `X_Q` exactly. Hence

\[
\log n_Q
=H(X_Q)
=H(C,D)
\le H(C)+H(D).
\tag{33}
\]

Taking the two independent minima proves `(14)`.

For a sequence with exponent `beta`, AF-227 gives

\[
\frac{E_Q(r_Q)}{\log n_Q}
\longrightarrow
(1-\beta)_+,
\tag{34}
\]

while `(12)` at zero error, with the harmless factor `1/2` in the radius, gives

\[
\frac{R_Q(r_Q/2,0)}{\log n_Q}
\longrightarrow
\min\{\beta,1\}.
\tag{35}
\]

The two coefficients add to one, proving `(15)`.

## Exact controls and boundaries

### This is deterministic one-shot localization, not Shannon's full rate-distortion function

`R_Q(r,delta)` minimizes the entropy of a deterministic mark for one finite source under an excess-error localization criterion. Shannon rate-distortion theory studies a broader asymptotic coding problem and can permit stochastic test channels. The classical theory supplies the correct surrounding language, but `(12)` is a source-specific one-shot asymptotic across growing prime cutoffs.

### Complement coloring is not the same as Körner graph-entropy splitting

Classical graph entropy has deep complement identities, including exact splitting for important perfect-graph regimes. Equations `(13)`--`(15)` concern **minimum chromatic entropy**, the one-shot coloring quantity already used in AF-227. Minimum chromatic entropy and Körner graph entropy are related but are not identical in general.

The inequality `(14)` is elementary and makes no novelty claim. Its use here is to expose what the two AF quantities retain: one coloring separates confusable nearby points, while the complementary coloring localizes the source well enough that the pair restores exact identity.

### The uniform cutoff law is load bearing

The factor `(1-delta)` in `(12)` comes from a uniform source. Under a nonuniform law, the optimal strategy can discard a small number of high- or low-probability source points very differently, and local occupancy cardinality no longer directly determines conditional entropy. No distribution-free phase law is claimed.

### Source coordinate and distortion are load bearing

The polynomial exponent arises from the specific coordinate `-log log p` and absolute source-space distortion. A different coordinate, metric, or distortion criterion can change both the occupancy exponent and the covering exponent.

### The theorem prices recoverability, not arithmetic meaning

A localization mark can carry almost full source identity while carrying no canonical rational-prime invariant. Conversely, a low-entropy coarse location mark can be cheap without preserving the discriminator needed by a later arithmetic operation. The theorem measures one recovery resource; it does not establish RH relevance.

### The first-order split does not determine additive terms

Equation `(15)` is an entropy-rate statement. It does not assert exact equality of the two minimum chromatic entropies at finite `Q`, nor does it identify optimal colorings or the `O(log log Q)` corrections.

## Prior art and novelty assessment

Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record* **7**, part 4, 142--163 (1959), is the classical origin of rate-distortion theory. Robert M. Gray and David L. Neuhoff, **“Quantization,”** *IEEE Transactions on Information Theory* **44**(6), 2325--2383 (1998), DOI `10.1109/18.720541`, surveys quantization, entropy-constrained coding, and the relationship to rate distortion.

Noga Alon and Alon Orlitsky, **“Source Coding and Graph Entropies,”** *IEEE Transactions on Information Theory* **42**(5), 1329--1339 (1996), DOI `10.1109/18.532875`, is direct prior art for one-shot source coding, chromatic entropy, and its relation to Körner graph entropy. János Körner and Katalin Marton, **“Graphs that Split Entropies,”** *SIAM Journal on Discrete Mathematics* **1**(1), 71--79 (1988), DOI `10.1137/0401008`, is direct prior art for complement-splitting questions in graph entropy.

No novelty is claimed for rate-distortion theory, entropy-constrained quantization, chromatic entropy, graph complements, or graph-entropy splitting. A targeted prior-art search located these established frameworks but did not locate the specific prime-tail one-shot phase law `(12)` or the AF-227/AF-228 asymptotic saturation `(15)`. Absence from that search is not evidence of priority. The durable Arithmetic Fidelity result is the exact category-specific synthesis built on AF-224--AF-227: the same shrinking source scale that makes proximity separation cheaper makes localization more expensive, and on polynomial scales their zero-error entropy rates add back to the full prime-source identity.

## Consequence for the research line

AF-227 shows that an `r_Q`-proper mark becomes entropy-cheap only after the source radius shrinks polynomially. AF-228 identifies the other side of that trade: at the same polynomial scale, **coarse localization consumes exactly the entropy fraction that proximity separation releases**, to first order.

This sharpens the current marked-translation frontier. A representation cannot be judged by mark cardinality or one entropy number in isolation. It must state which recovery task the mark performs. Separating nearby source points and localizing the source are complementary resources; if both are needed strongly enough to restore exact prime-source identity, their combined zero-error entropy remains asymptotically `log pi(Q)` across the entire polynomial resolution family. Any genuinely cheaper repair must therefore exploit arithmetic structure beyond generic source identity, change the admissible distortion/recovery task, or prove that one of these two generic recovery duties is unnecessary.