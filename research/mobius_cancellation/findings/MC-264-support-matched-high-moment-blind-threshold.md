# MC-264 — Support-matched high moments cross the single-blind threshold

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CANDIDATE-NEW-STRUCTURE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-parity notation of `MC-242`, `MC-253`, `MC-262`, and `MC-263`. Let

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad
\mathcal R_y=\{r:y<r\le2y,\ r\text{ prime}\},
\]

write

\[
k_y=|\mathcal P_y|,
\qquad
N_y=|\mathcal R_y|,
\]

and for `T\subset\mathcal R_y`, `|T|=t`, define

\[
B_y(T)=\sum_{p\in\mathcal P_y}\prod_{r\in T}\left(\frac pr\right).
\tag{1}
\]

A blind relation supported on `T` has `B_y(T)=k_y`. If

\[
A_y(t)=\#\{T\in\tbinom{\mathcal R_y}{t}:B_y(T)=k_y\}
\]

and

\[
S_{2m,y}(t)=\sum_{|T|=t}|B_y(T)|^{2m},
\]

then for every integer `m>=1`, exactly

\[
\boxed{A_y(t)k_y^{2m}\le S_{2m,y}(t).}
\tag{2}
\]

`MC-263` showed that the second moment (`m=1`) is far too coarse at the first unresolved support scale `t\asymp\log\log y`: a family-size `L^2` estimate must be super-polynomially sharper than its natural diagonal scale to exclude even one blind subset. The higher-moment calculation changes that threshold sharply.

Raise `(1)` to the `m`-th power and reduce products modulo squares. There are nonnegative coefficients `c_{m,y}(u)`, indexed by square-free products of primes in `\mathcal P_y`, such that

\[
B_y(T)^m
=
\sum_u c_{m,y}(u)
\prod_{r\in T}\left(\frac ur\right).
\tag{3}
\]

Their quadratic mass satisfies the exact sandwich

\[
\boxed{
(2m-1)!!\,(k_y)_m
\le
D_{m,y}:=\sum_u c_{m,y}(u)^2
\le
(2m-1)!!\,k_y^m.
}
\tag{4}
\]

Hence whenever `m^2=o(k_y)`, in particular throughout `m=O(\log\log y)`,

\[
D_{m,y}=(1+o(1))(2m-1)!!\,k_y^m.
\tag{5}
\]

Now suppose a future shell-specific theorem had the natural sparse-family form

\[
\boxed{
S_{2m,y}(t)
\le
L_y\binom{N_y}{t}D_{m,y},
}
\tag{6}
\]

where `L_y` is the analytic loss. This is not proved here; `(6)` is the precise candidate inequality whose strength can now be calibrated against one blind atom.

For `m=t`, the right side of `(6)` divided by `k_y^{2t}` has natural scale

\[
L_y\frac{\binom{N_y}{t}(2t-1)!!k_y^t}{k_y^{2t}}
=
(1+o(1))L_y\frac{(2t-1)!!}{t!}
=
(1+o(1))L_y\frac{\binom{2t}{t}}{2^t}.
\tag{7}
\]

Thus

\[
\boxed{
\text{moment order }2t\text{ is still too small at natural diagonal scale:}
\quad
\frac{\binom{2t}{t}}{2^t}
\sim
\frac{2^t}{\sqrt{\pi t}}.
}
\tag{8}
\]

But taking only **one additional tensor power**, `m=t+1`, gives

\[
\frac{\binom{N_y}{t}D_{t+1,y}}{k_y^{2t+2}}
\le
(1+o(1))
\frac{(2t+1)!!}{t!\,k_y}
\sim
\frac{2^{t+1}\sqrt{t/\pi}}{k_y}.
\tag{9}
\]

At the first unresolved support scale from `MC-242`,

\[
t=
\left(\frac1{\log2}+o(1)\right)\log\log y,
\tag{10}
\]

we have `2^t=(\log y)^{1+o(1)}` and `k_y\sim y/\log y`. Therefore

\[
\boxed{
\frac{\binom{N_y}{t}D_{t+1,y}}{k_y^{2t+2}}
\le
\frac{(\log y)^{2+o(1)}\sqrt{\log\log y}}{y}
\longrightarrow0.
}
\tag{11}
\]

Consequently a shell-specific estimate of the form `(6)` at `m=t+1` would already rule out every weight-`t` blind relation provided its loss satisfies

\[
L_y
=o\!\left(
\frac{k_y}{2^t\sqrt t}
\right).
\tag{12}
\]

At `(10)` this permits, for example, any polylogarithmic loss and in fact losses as large as

\[
y^{1-o(1)}/(\log y)^2
\]

up to the displayed `\sqrt{\log\log y}` factor. The family-size obstruction in `MC-263` is therefore not an intrinsic obstruction to all moment methods. It is specifically a **low-moment obstruction**. Once the moment order tracks the possible blind support, the single exceptional atom becomes detectable with substantial quantitative slack.

The missing theorem is equally precise: one must establish a sparse-shell high-moment estimate such as `(6)` for `m\asymp t\asymp\log\log y`. Standard all-squarefree-moduli quadratic large-sieve tensorization does not do this, because after raising to the `m`-th power the Dirichlet-polynomial coefficient range reaches roughly `y^m`, while the shell moduli have size roughly `y^t`; at `m=t+1` the generic `(M+N)` large-sieve cost is already dominated by the coefficient-length term and loses the shell-family advantage.

Thus the current frontier is no longer vaguely “find a stronger large sieve.” It is:

\[
\boxed{
\text{control the }2(t+1)\text{-th moment directly over the fixed-weight shell-product family,}
}
\tag{13}
\]

or prove that such control is impossible at the required scale.

No blind relation is excluded here, no new rank bound is proved, and no estimate for `M(X)` follows.

## 1. Exact quadratic mass after tensorization

Let an ordered `m`-tuple `(p_1,\ldots,p_m)\in\mathcal P_y^m` contribute to the square-free kernel

\[
u=\operatorname{sf}(p_1\cdots p_m).
\]

Define `c_{m,y}(u)` to be the number of ordered tuples with that square-free kernel. Since every shell prime `r>y`, no `r` divides the product, and quadratic-character multiplicativity gives `(3)`.

The quantity

\[
D_{m,y}=\sum_u c_{m,y}(u)^2
\]

counts ordered pairs of `m`-tuples with the same parity vector of prime multiplicities. Equivalently it counts words of length `2m` on an alphabet of size `k_y` in which every letter occurs an even number of times.

For the lower bound in `(4)`, take words using exactly `m` distinct letters, each twice. Choose the `m` distinct letters and distribute their two copies among the `2m` positions. This gives

\[
\binom{k_y}{m}\frac{(2m)!}{2^m}
=(2m-1)!!\,(k_y)_m.
\tag{14}
\]

For the upper bound, every even-multiplicity word admits at least one perfect pairing of the `2m` positions in which paired positions carry the same letter. There are `(2m-1)!!` pairings and at most `k_y^m` assignments of letters to the pairs. Counting by `(pairing, assignment)` therefore overcounts all admissible words and gives

\[
D_{m,y}\le(2m-1)!!k_y^m.
\tag{15}
\]

Finally `(k_y)_m/k_y^m=1+o(1)` when `m^2=o(k_y)`, proving `(5)`.

The double factorial is essential. Treating the tensor coefficients as though ordinary product equality, rather than equality modulo squares, were the only diagonal would incorrectly produce `m!k_y^m`. Quadratic characters identify all products with the same square-free kernel, and the natural diagonal is therefore the Gaussian/Rademacher moment `(2m-1)!!k_y^m`.

## 2. The fixed-weight shell sum is exactly a Krawtchouk kernel

Equation `(6)` also has an exact harmonic reformulation. For two square-free coefficient indices `u,v`, define their shell-signature distance

\[
d_y(u,v)
=
\#\left\{r\in\mathcal R_y:
\left(\frac{uv}{r}\right)=-1
\right\}.
\tag{16}
\]

For `N=N_y`, let

\[
K_t(d;N)
=
\sum_{j=0}^t
(-1)^j
\binom dj
\binom{N-d}{t-j}
\tag{17}
\]

be the binary Krawtchouk polynomial. Then simply summing the product of the `N` signs over all `t`-subsets gives

\[
\boxed{
\sum_{|T|=t}
\prod_{r\in T}\left(\frac{uv}{r}\right)
=K_t(d_y(u,v);N_y).
}
\tag{18}
\]

Expanding `(3)` therefore yields the exact identity

\[
\boxed{
S_{2m,y}(t)
=
\sum_{u,v}
 c_{m,y}(u)c_{m,y}(v)
 K_t(d_y(u,v);N_y).
}
\tag{19}
\]

The literal diagonal has `d_y(u,u)=0` and

\[
K_t(0;N_y)=\binom{N_y}{t},
\]

which explains the family-size diagonal term in `(6)`. Formula `(19)` identifies the actual missing analytic object: the **off-diagonal Krawtchouk-weighted distribution of shell Legendre-signature distances between square-free kernels of `m`-fold lower-prime products**.

This is stronger and more specific than asking for pairwise column balance. The order `t` Krawtchouk kernel is exactly the fixed-weight Fourier layer that can see a support-`t` blind relation, while the tensor order `m=t+1` supplies enough moment amplification to make one such relation visible above the natural diagonal mass.

## 3. Why the ordinary quadratic large sieve does not already prove the candidate estimate

One may try to apply Heath-Brown/Liu after `(3)`. The square-free kernel `u` is at most `y^m`, while every shell modulus

\[
q_T=\prod_{r\in T}r
\]

has size between `y^t` and `(2y)^t`. Embedding the shell products into all square-free moduli up to `(2y)^t` and applying the usual quadratic large sieve therefore incurs a leading scale comparable to

\[
\bigl(y^t+y^m\bigr)D_{m,y}
\tag{20}
\]

apart from its explicit subpower loss.

At the useful moment `m=t+1`, `(20)` is dominated by `y^{t+1}D_{m,y}`. The desired shell-family scale in `(6)` is instead

\[
\binom{N_y}{t}D_{m,y}
\asymp
\frac1{t!}
\left(\frac y{\log y}\right)^t
D_{m,y}.
\tag{21}
\]

Their ratio is at least of order

\[
y\,t!(\log y)^t,
\]

before the explicit `\varepsilon`-loss audited in `MC-262` is paid. Thus ordinary tensorization followed by the all-moduli quadratic large sieve destroys precisely the sparse-family saving needed by `(11)`.

This is compatible with the broader high-moment literature. High moments combined with quadratic large-sieve input are a standard tool for distributions of quadratic character sums, but successful arguments tailor the moment order and coefficient length to the character family rather than obtaining `(6)` automatically. Youness Lamzouri's *The distribution of large quadratic character sums and applications*, Algebra & Number Theory 18 (2024), 2091--2131, DOI `10.2140/ant.2024.18.2091`, explicitly uses scale-dependent high moments together with quadratic-large-sieve estimates in this way. That literature is evidence that the technique is classical, not that the present sparse shell estimate is known.

## 4. Prior-art and novelty audit

No novelty is claimed for moment amplification, the quadratic large sieve, Walsh/Fourier analysis on the Boolean cube, or Krawtchouk polynomials.

The fixed-weight identity `(18)` is the standard Hamming-scheme/Krawtchouk transform: the sum of Walsh characters of weight `t` depends only on Hamming distance and equals `K_t`. A modern coding-theory reference making this relationship explicit is Alex Samorodnitsky, *Weight distribution of random linear codes and Krawtchouk polynomials*, Random Structures & Algorithms 64 (2024), DOI `10.1002/rsa.21214`.

The relevant quadratic-large-sieve inputs remain D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), 235--275, DOI `10.4064/aa-72-3-235-275`, and Zihao Liu, *Explicit quadratic large sieve inequality*, Acta Arithmetica 223 (2026), 227--252, DOI `10.4064/aa250722-27-1`; their consequences for the present shell were audited in `MC-253` and `MC-262`.

A targeted literature search through 13 September 2026 found high-moment quadratic-character methods and extensive Krawtchouk/coding-theory machinery, but no theorem giving the specific fixed-weight shell-product estimate `(6)` uniformly for `m,t\asymp\log\log y`. The durable Mathia delta is therefore not a claimed new analytic theorem. It is the exact **threshold calculation and kernel identification**: second moments are provably blind at the live support scale (`MC-263`), moment order `2t` remains naturally above one blind atom because of the quadratic/Rademacher diagonal, while order `2(t+1)` has enough amplification that a shell-family diagonal-scale estimate with very substantial loss would exclude that atom.

## 5. Boundaries and decisive test

- **Candidate inequality, not theorem.** Equation `(6)` is the missing analytic input. Nothing here establishes it for the arithmetic shell family.
- **Quadratic diagonal audited.** The correct natural mass is `(2m-1)!!k_y^m`, not `m!k_y^m`; square-kernel collisions are included in `(4)`.
- **Exact fixed-weight kernel.** Equation `(19)` has no probabilistic independence assumption. All arithmetic difficulty sits in the off-diagonal Legendre-signature distances.
- **No rank inference.** Even proving `(6)` at one support order would exclude blind relations of that weight; it would not by itself prove full rank unless the estimate covered every still-admissible weight.
- **No generic-large-sieve shortcut.** The coefficient-length term at `m=t+1` is parametrically too large under the all-squarefree-moduli embedding.
- **No RH-scale conclusion.** This is a generation-frontier result inside the rough Möbius decomposition. Any later route to `M(X)` still needs the already-audited transfer from generation/signed rough cancellation to the global zero mode.

The decisive next test is now concrete: derive either an upper bound for the off-diagonal part of `(19)` strong enough to imply `(6)` with

\[
L_y=o\!\left(\frac{k_y}{2^t\sqrt t}\right)
\]

at `t=(1/\log2+o(1))\log\log y`, or construct an admissible arithmetic configuration showing that the Krawtchouk off-diagonal mass can remain as large as a blind atom despite the shell constraints. Either outcome materially settles whether high moments genuinely evade the `MC-263` single-blind `L^2` barrier.