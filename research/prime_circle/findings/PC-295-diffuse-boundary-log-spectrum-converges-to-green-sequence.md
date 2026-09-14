# PC-295 — diffuse boundary-log spectrum converges to the classical Green sequence

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the complete one-profile boundary-log singular-spectrum shape left open by PC-294.

PC-294 proves that the complete normalized boundary-log Hilbert-Schmidt mass is source-universal for every sufficiently diffuse source, but deliberately leaves open whether the **distribution of that mass among singular values** can retain an order-one prime-specific shape. That remaining branch also collapses in the natural absolute ordered-spectrum topology.

Let `q` run through odd primes, let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and use the exact PC-283 boundary-renormalized logarithmic profile

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0).
\tag{1}
\]

For source residues `p,r` define

\[
K_{q,B}^{p,r}(h,k)=k_q(ph+rk),
\qquad h,k\in H_B.
\tag{2}
\]

Let `mu_q` be any probability measure on `Z/qZ`, choose `p,r` independently with law `mu_q`, and write

\[
\beta_q:=\|\mu_q\|_\infty.
\tag{3}
\]

Assume

\[
\boxed{
N\to\infty,
\qquad
(\log q)^2\sqrt{\frac{q\beta_q}{N}}\longrightarrow0.
}
\tag{4}
\]

Define the deterministic length-`N` sequence

\[
\boxed{
s_j^{(N)}:=\frac1{2\lceil j/2\rceil},
\qquad 1\le j\le N.
}
\tag{5}
\]

Thus

\[
s^{(N)}=(1/2,1/2,1/4,1/4,1/6,1/6,\ldots)
\]

truncated after `N` entries. If `Sigma(A)` denotes the decreasing ordered singular-value vector of `A`, then

\[
\boxed{
\mathbb E_{p,r\sim\mu_q}
\left\|
\Sigma\!\left(\frac{K_{q,B}^{p,r}}N\right)
-s^{(N)}
\right\|_{\ell^\infty}
\longrightarrow0.
}
\tag{6}
\]

Equivalently, the complete source-averaged ordered singular-spectrum law converges in `W_1^{(ell^infinity)}` to the point mass at the deterministic Green sequence (5).

For prime-scale diffuse sources,

\[
\beta_q=O\!\left(\frac{\log q}{q}\right),
\]

condition (4) is exactly satisfied whenever

\[
\boxed{
\frac{N}{(\log q)^5}\longrightarrow\infty.
}
\tag{7}
\]

Hence the normalized prime source and the count-matched Li-grid control of PC-290 both have the **same complete absolute singular-spectrum limit**, unconditionally, throughout this range. In particular this includes the square-root frontier `N~sqrt(q)` that PC-290 could only approach from below by RH transport.

The limiting sequence is not a new arithmetic spectrum. It is precisely the singular spectrum of the classical mean-zero logarithmic Green/single-layer operator on the circle whose Fourier multiplier is `-1/(2|m|)`, already identified in PC-283. Thus the remaining one-profile boundary-log spectral shape at square-root resolution classicalizes completely after diffuse source averaging.

## 1. Exact rank-one Fourier decomposition

Use the unnormalized finite Fourier transform

\[
\widehat k_q(m)
=
\sum_{t\bmod q}k_q(t)e^{-2\pi i mt/q}
\]

and set

\[
a_q(m):=\frac{\widehat k_q(m)}q.
\tag{8}
\]

PC-283 gives

\[
a_q(0)=0,
\qquad
a_q(m)<0\quad(m\ne0),
\tag{9}
\]

and, for every fixed positive integer `m`,

\[
\boxed{
a_q(m)=a_q(q-m)\longrightarrow-\frac1{2m}.}
\tag{10}
\]

It also gives the exact Wiener mass

\[
\boxed{
\sum_{m\bmod q}|a_q(m)|=\log q.
}
\tag{11}
\]

For each Fourier mode define unit vectors in `C^N`,

\[
x_{m,p}(h):=N^{-1/2}e^{2\pi i mph/q},
\qquad
z_{m,r}(k):=N^{-1/2}e^{-2\pi i mrk/q}.
\tag{12}
\]

Fourier inversion of (1) gives the exact matrix identity

\[
\boxed{
\frac{K_{q,B}^{p,r}}N
=
\sum_{m\bmod q}
a_q(m)x_{m,p}z_{m,r}^{*}.
}
\tag{13}
\]

Thus the finite section is a superposition of rank-one Fourier channels. The only issue is whether the source-dilated mode vectors remain sufficiently orthogonal, and whether the infinitely many higher channels can collectively retain source-specific operator mass.

## 2. Diffuse dilations orthogonalize every fixed set of Fourier modes

For nonzero `d mod q` put

\[
c_d(p):=
\frac1N\sum_{h\in H_B}e^{2\pi i dph/q}.
\tag{14}
\]

If `m!=n`, then

\[
\langle x_{m,p},x_{n,p}\rangle=c_{n-m}(p).
\tag{15}
\]

Because `q` is prime and `d!=0`, multiplication by `d` permutes `Z/qZ`. Finite Parseval for the interval indicator gives the exact identity

\[
\sum_{p\bmod q}|c_d(p)|^2=\frac qN.
\tag{16}
\]

Therefore every source satisfying (3) obeys

\[
\boxed{
\mathbb E_{p\sim\mu_q}|c_d(p)|^2
\le
\beta_q\frac qN.
}
\tag{17}
\]

Fix `M` and let

\[
S_M:=\{\pm1,\ldots,\pm M\}\subset\mathbb Z/q\mathbb Z
\]

for `q>2M`. Let `X_{p,M}` have columns `x_{m,p}`, `m in S_M`. Its Gram matrix satisfies

\[
\boxed{
\mathbb E
\|X_{p,M}^*X_{p,M}-I_{2M}\|_F^2
\le
2M(2M-1)\frac{q\beta_q}{N}.
}
\tag{18}
\]

The identical estimate holds for the columns `z_{m,r}`. Condition (4) implies `q beta_q/N ->0`, so for every fixed `M` the left and right Fourier families become orthonormal in mean square.

Let

\[
A_{q,M}^{p,r}
:=
\sum_{m\in S_M}
a_q(m)x_{m,p}z_{m,r}^*.
\tag{19}
\]

On the event that both Gram matrices lie within `1/2` of the identity in operator norm, polar orthonormalization changes `X_{p,M}` and `Z_{r,M}` by `O_M` of their Gram errors. The resulting rank-`2M` matrix has singular values exactly

\[
\{|a_q(m)|:m\in S_M\}.
\]

Equation (18), Cauchy-Schwarz, and Markov's inequality therefore give

\[
\boxed{
\mathbb E
\left\|
\Sigma(A_{q,M}^{p,r})
-\operatorname{sort}\bigl(\{|a_q(m)|:m\in S_M\}\cup\{0\}^{N-2M}\bigr)
\right\|_\infty
\longrightarrow0
}
\tag{20}
\]

for each fixed `M`. By (10), the nonzero target in (20) converges to

\[
(1/2,1/2,1/4,1/4,\ldots,1/(2M),1/(2M)).
\tag{21}
\]

This is already the classical circle Green spectrum on every fixed finite set of modes.

## 3. The Fourier tail has universally vanishing operator norm

The nontrivial step is to control all modes outside `S_M` without assuming random independent sample nodes. Let

\[
R_{q,M}^{p,r}
:=
\sum_{m\notin S_M}
a_q(m)x_{m,p}z_{m,r}^*.
\tag{22}
\]

The zero mode contributes nothing. Define, exactly as in PC-294,

\[
A_{\mu_q}(d)
:=
\frac1N\sum_{h\in H_B}\widehat\mu_q(dh).
\tag{23}
\]

Symmetry of `H_B` makes `A_mu(d)` real. Expanding the Frobenius norm of (22) and averaging the two independent source coordinates gives the exact identity

\[
\boxed{
\mathbb E\|R_{q,M}^{p,r}\|_F^2
=
\sum_{m,n\notin S_M}
a_q(m)a_q(n)A_{\mu_q}(n-m)^2.
}
\tag{24}
\]

The common sign in (9) is crucial: every coefficient product `a_q(m)a_q(n)` is nonnegative.

Let `u_q` be the uniform law on `Z/qZ`. PC-294 proves for every nonzero `d`

\[
\left|A_{\mu_q}(d)-A_{u_q}(d)\right|
\le
\delta_q,
\qquad
\delta_q:=\sqrt{\frac{q\beta_q}{N}},
\tag{25}
\]

while

\[
A_{u_q}(0)=1,
\qquad
A_{u_q}(d)=\frac1N\quad(d\ne0).
\tag{26}
\]

Since both coefficients have modulus at most one,

\[
|A_{\mu_q}(d)^2-A_{u_q}(d)^2|
\le2\delta_q
\quad(d\ne0).
\tag{27}
\]

Using (11) in (24) therefore yields, for **every** Fourier subset and in particular for the tail,

\[
\boxed{
\left|
\mathbb E_{\mu_q}\|R_{q,M}\|_F^2
-
\mathbb E_{u_q}\|R_{q,M}\|_F^2
\right|
\le
2\delta_q(\log q)^2.
}
\tag{28}
\]

Under the uniform source, (24) is explicit:

\[
\boxed{
\mathbb E_{u_q}\|R_{q,M}\|_F^2
=
\left(1-\frac1{N^2}\right)
\sum_{m\notin S_M}|a_q(m)|^2
+
\frac1{N^2}
\left(\sum_{m\notin S_M}a_q(m)\right)^2.
}
\tag{29}
\]

The last term is at most `(log q)^2/N^2` by (11).

Finite Parseval gives

\[
\sum_{m\bmod q}|a_q(m)|^2
=
\frac1q\sum_{t\bmod q}k_q(t)^2.
\tag{30}
\]

PC-294 identifies the limit of the right side as `pi^2/12`. Combining (10) and (30), for every fixed `M`,

\[
\boxed{
\sum_{m\notin S_M}|a_q(m)|^2
\longrightarrow
R_M
:=
\frac{\pi^2}{12}
-
\frac12\sum_{j=1}^{M}\frac1{j^2}
=
\frac12\sum_{j>M}\frac1{j^2}.
}
\tag{31}
\]

Condition (4) makes the error in (28) vanish and, because `beta_q>=1/q`, also forces `(log q)/N ->0`. Thus Jensen's inequality gives

\[
\boxed{
\limsup_{q\to\infty}
\mathbb E\|R_{q,M}^{p,r}\|_{op}
\le
\limsup
\mathbb E\|R_{q,M}^{p,r}\|_F
\le
\sqrt{R_M}.
}
\tag{32}
\]

Finally `R_M ->0`. The entire high-frequency sector is therefore negligible in **operator norm after source averaging**, even though it carries the tail of the fixed Hilbert-Schmidt mass before `M` is sent to infinity.

## 4. Completion of the ordered-spectrum limit

Singular values are 1-Lipschitz under operator-norm perturbations, so (19), (22), and (32) imply

\[
\limsup_{q\to\infty}
\mathbb E
\left\|
\Sigma(K_{q,B}^{p,r}/N)-
\Sigma(A_{q,M}^{p,r})
\right\|_\infty
\le\sqrt{R_M}.
\tag{33}
\]

Equation (20) replaces the low-mode matrix by its deterministic finite multiplier list. Equation (10) then replaces that list by (21). The infinite Green sequence differs from the finite list padded with zeros by exactly

\[
\frac1{2(M+1)}
\]

in `ell^infinity`. Hence

\[
\boxed{
\limsup_{q\to\infty}
\mathbb E
\left\|
\Sigma(K_{q,B}^{p,r}/N)-s^{(N)}
\right\|_\infty
\le
\sqrt{R_M}+\frac1{2(M+1)}.
}
\tag{34}
\]

for every fixed `M`. Sending `M -> infinity` proves (6).

This argument explains why PC-294's value `pi^2/12` was already suggestive but not sufficient by itself. The identity

\[
\frac{\pi^2}{12}
=
2\sum_{m\ge1}\frac1{(2m)^2}
\]

is exactly the Hilbert-Schmidt mass of the limiting Green sequence. What was still required was to prove that diffuse source dilations asymptotically orthogonalize each fixed Fourier block and that the remaining Fourier tail is operator-small. Equations (18) and (28)--(32) supply those two missing steps.

## 5. Prime and matched-control consequences

For the normalized prime source, the prime number theorem gives

\[
\beta_q=\frac1{M_q}
\asymp\frac{\log q}{q}.
\tag{35}
\]

The count-matched Li-grid control of PC-290 has the same maximal-atom order. Therefore both satisfy (4) whenever (7) holds, and in particular at `N~sqrt(q)`.

Let `rho_{q,B}^{mu,log}` denote the law of the complete normalized ordered singular vector under the independent product source `mu_q tensor mu_q`. From (6),

\[
\boxed{
W_1^{(\ell^\infty)}
\left(
rho_{q,B}^{\mu,log},
\delta_{s^{(N)}}
\right)
\longrightarrow0.
}
\tag{36}
\]

Consequently any two source families satisfying (4) obey

\[
\boxed{
W_1^{(\ell^\infty)}
\left(
rho_{q,B}^{\mu,log},
rho_{q,B}^{\nu,log}
\right)
\longrightarrow0.
}
\tag{37}
\]

No RH input and no source-position theorem is used. The arithmetic locations disappear because the source enters only through dilations of Fourier sampling vectors, while diffuseness controls their averaged Gram matrices and PC-283's same-sign multiplier controls the full tail.

The canonical prime law uses distinct ordered source pairs. Conditioning the uniform prime product law on `p!=r` changes an expectation of any `ell^infinity`-bounded spectral observable by at most the diagonal probability `1/M_q` times the spectral diameter. Since every entry of `K/N` has modulus at most `log q/N` times `N` at the Frobenius level, `||K/N||_op<=log q`, so the conditioning cost is

\[
O\!\left(\frac{\log q}{M_q}\right)
=O\!\left(\frac{(\log q)^2}{q}\right)
=o(1).
\tag{38}
\]

Thus the same limit holds for the distinct prime-pair spectral law used elsewhere in the line.

## 6. Prior-art and novelty audit

The limiting operator is classical. PC-283 already identifies the continuum boundary log-sine convolution with the mean-zero logarithmic single-layer/Green operator on the circle, whose nonzero Fourier multipliers are `-1/(2|m|)`. Therefore the sequence (5) is classical harmonic/potential-theory data, not a new zeta spectrum.

The approximation architecture is also adjacent to established theory. Slepian's discrete prolate theory, partial Fourier/Vandermonde conditioning, Nyström approximation of compact integral operators, random sampling of trigonometric polynomials, and restricted-isometry results for subsampled Fourier matrices all study variants of finite Fourier sampling and spectral approximation. Targeted checks included:

- David Slepian, **Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case**, *Bell System Technical Journal* 57:5 (1978), 1371–1430;
- Richard F. Bass and Karlheinz Gröchenig, **Random Sampling of Multivariate Trigonometric Polynomials**, *SIAM Journal on Mathematical Analysis* 36:3 (2004/2005), 773–795, DOI `10.1137/S0036141003432316`;
- Dmitry Batenkov, Laurent Demanet, Gil Goldman and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`;
- Ishay Haviv and Oded Regev, **The Restricted Isometry Property of Subsampled Fourier Matrices**, *SODA 2016*, 288–297, DOI `10.1137/1.9781611974331.ch22`.

Those works confirm that near-orthogonality and singular-value stability of Fourier sampling systems are classical themes. They do not serve as load-bearing inputs here: equations (16)--(18) are a one-line finite Parseval argument specialized to a single random/diffuse multiplicative dilation, while the tail control uses the exact same-sign log-sine multiplier already established in PC-283/PC-294. No new `SOURCES.md` dependency is required.

No novelty is claimed for the Green spectrum, Fourier-mode orthogonality, matrix perturbation, Nyström/sampling convergence, or the general principle that compact convolution spectra can be approximated by finite sections. The durable project-local delta is narrower: **the exact Prime-Circle source-dilated boundary-log matrices converge, under only maximal-atom diffuseness at the same threshold as PC-294, to that classical Green singular sequence in the complete absolute ordered-spectrum topology.** This closes the spectral-shape escape that PC-294 explicitly left open.

## 7. Boundaries and falsification tests

Equation (6) is strong in absolute `ell^infinity` topology but it is not a relative small-singular-value theorem. Since

\[
s_N^{(N)}\asymp\frac1N,
\]

an `o(1)` absolute error does not control determinants, log-determinants, inverse moments, condition numbers, or a rescaled microscopic law near zero. Such observables can amplify changes far below the absolute scale resolved here.

The result also does not control singular vectors, source-conditioned exceptional pairs, raw phase information, directional/non-normal observables, several profiles retained jointly before SVD, cross-source correlations beyond the product average, or cross-level operators. PC-292's exceptional same-source Hankel behavior remains a valid worst-case phenomenon; it is simply absent from the diffuse averaged absolute spectrum.

The argument has direct falsification points:

1. violate the exact rank-one decomposition (13) by direct DFT reconstruction;
2. find nonzero `d` for which the finite Parseval identity (16) fails;
3. violate the exact averaged tail formula (24);
4. produce a Fourier-tail energy exceeding (28)--(29) under a source with the stated maximal atom;
5. keep `M` fixed while a low-mode Gram matrix stays non-orthogonal in mean square despite `q beta_q/N ->0`;
6. find a source satisfying (4) for which the normalized ordered singular vector remains at order-one `ell^infinity` distance from (5).

Small-prime numerical checks of (13), (24), and the emerging pairs `(1/2,1/2),(1/4,1/4),...` agree with the exact identities, but no numerical input is used in the proof.

The principal surviving boundary is therefore sharper than after PC-294. **For one boundary-log profile and diffuse source averaging, neither local residues, total Hilbert-Schmidt mass, nor the complete absolute ordered singular-value shape can carry an order-one prime-specific signal once `N/(log q)^5 -> infinity`.** Any RH-facing information still present at this stage must live in representation-richer data: relative/microscopic small-singular structure, singular vectors or phases, non-product/extremal source statistics, joint noncommuting profiles, or genuine cross-level coupling before the one-profile SVD compression.