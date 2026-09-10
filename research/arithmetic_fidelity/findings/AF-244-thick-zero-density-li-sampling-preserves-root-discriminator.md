# AF-244 — thick zero-density Li sampling preserves the root discriminator

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `RH-SUFFICIENT-QUOTIENT`, `OUTPUT-SAMPLING`, `LOCAL-OBSERVABILITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

For a finite exponential mode, retaining a positive density of output indices is not necessary to preserve its exponential root-rate discriminator. A much weaker local-observability condition is sufficient.

Let

\[
a_n=q^nF(n)+r_n,
\qquad q>1,
\tag{1}
\]

where

\[
F(n)=\sum_{j=1}^m c_j u_j^n,
\qquad |u_j|=1,
\tag{2}
\]

with distinct `u_j` and not all `c_j` zero, and assume

\[
\limsup_{n\to\infty}|r_n|^{1/n}<q.
\tag{3}
\]

If `S\subset\mathbb N` is **thick**, meaning that it contains intervals of consecutive integers of arbitrarily large finite length, then

\[
\boxed{
\limsup_{\substack{n\to\infty\\ n\in S}} |a_n|^{1/n}=q.
}
\tag{4}
\]

Applied to the Li coefficients `\lambda_n`, this yields the following exact sparse-output criterion:

> For every thick set `S\subset\mathbb N`, the Riemann hypothesis is equivalent to
> \[
> \limsup_{\substack{n\to\infty\\ n\in S}}|\lambda_n|^{1/n}\le1.
> \tag{5}
> \]

Moreover, `S` may have natural density zero. For example,

\[
S=\bigcup_{k\ge1}
\left([2^{k^2},\,2^{k^2}+k-1]\cap\mathbb N\right)
\tag{6}
\]

is thick and has density zero, yet `(5)` is still equivalent to RH.

The result concerns **sampling of already formed Li outputs**. It does not reduce the source depth or arithmetic information needed to compute a sampled high-index `\lambda_n`; in particular it does not undo the source-access and cancellation obstructions of AF-238--AF-243.

## Why it matters

Arithmetic Fidelity has repeatedly separated the amount of retained data from the structure needed to preserve a discriminator. This result makes that separation exact in a zeta-relevant setting.

For finite exponential modes, asymptotic density is the wrong resource measure: an output set can discard an asymptotic fraction `1` of the sequence and still preserve the full exponential root rate. What matters here is instead a form of **local observability completeness**: sufficiently long consecutive windows prevent every nonzero finite exponential polynomial from remaining small throughout all retained observations.

This supplies a positive counterpart to the recent source-compression obstructions. AF-238--AF-243 show that aggressively reducing the *inputs* to a Li coefficient can destroy or contaminate the cancellation needed for interpretation. AF-244 shows that, once the globally cancelled Li outputs exist, they can be sampled extremely sparsely without losing the off-critical exponential discriminator, provided the sampling geometry retains complete finite local windows.

## Derivation / evidence

### 1. Thick sets observe every nonzero finite exponential mode

For `(2)`, form the `m\times m` Vandermonde matrix

\[
V=(u_j^k)_{0\le k<m,\ 1\le j\le m}.
\tag{7}
\]

Since the `u_j` are distinct, `V` is invertible. For every integer `N`,

\[
\begin{pmatrix}
F(N)\\
F(N+1)\\
\vdots\\
F(N+m-1)
\end{pmatrix}
=
V
\begin{pmatrix}
c_1u_1^N\\
c_2u_2^N\\
\vdots\\
c_mu_m^N
\end{pmatrix}.
\tag{8}
\]

The Euclidean norm of the rightmost coefficient vector is independent of `N`, because `|u_j|=1`. Invertibility of `V` therefore gives a constant `C>0`, depending only on the fixed mode `(u_j,c_j)`, such that

\[
\max_{0\le k<m}|F(N+k)|\ge C
\qquad\text{for every }N.
\tag{9}
\]

A thick set contains arbitrarily far-out intervals of length at least `m`. In each such retained block, `(9)` supplies an index `n\in S` with `|F(n)|\ge C`.

Choose `\eta` satisfying

\[
\limsup |r_n|^{1/n}<\eta<q.
\tag{10}
\]

Then eventually `|r_n|\le\eta^n`, and along the retained indices supplied by `(9)`,

\[
|a_n|
\ge Cq^n-\eta^n
\ge \frac C2 q^n
\tag{11}
\]

for all sufficiently large such `n`. Hence the restricted limsup is at least `q`. Since `F` is bounded and `(3)` makes the remainder exponentially smaller, the unrestricted limsup is at most `q`, proving `(4)`.

The proof uses no density estimate. It uses only a finite-window uniqueness property of exponential polynomials.

### 2. Off-critical zeros give a finite dominant exponential mode for Li coefficients

Use the classical Keiper--Li generating function

\[
G(z)
:=
\frac{d}{dz}\log\xi\!\left(\frac1{1-z}\right)
=
\sum_{n\ge1}\lambda_n z^{n-1},
\tag{12}
\]

where `\xi` is the completed Riemann xi function. A nontrivial zero `\rho` of `\xi` maps to a pole of `G` at

\[
\alpha_\rho=1-\frac1\rho.
\tag{13}
\]

The elementary identity

\[
|\rho-1|^2-|\rho|^2=1-2\Re\rho
\tag{14}
\]

shows that

\[
|\alpha_\rho|<1
\iff
\Re\rho>\frac12,
\qquad
|\alpha_\rho|=1
\iff
\Re\rho=\frac12.
\tag{15}
\]

If RH is false, functional-equation symmetry supplies at least one zero with real part greater than `1/2`, so `G` has at least one pole in the open unit disk. Let

\[
r_0:=\min_{\Re\rho>1/2}|\alpha_\rho|<1.
\tag{16}
\]

The minimum is attained. Indeed `|\alpha_\rho|\le r<1` implies

\[
\rho=\frac1{1-\alpha_\rho}
\]

lies in a bounded region, and an entire function has only finitely many zeros in a compact set unless it vanishes identically. Thus only finitely many zero-poles of `G` occur on the circle `|z|=r_0`.

Choose `R` with

\[
r_0<R<1
\tag{17}
\]

such that there is no pole modulus in `(r_0,R]`. Subtract the principal parts of the finitely many poles `\alpha_1,\ldots,\alpha_m` with `|\alpha_j|=r_0`. If their zero multiplicities are `m_j\ge1`, the logarithmic derivative has residue `m_j`, so

\[
G(z)
=
\sum_{j=1}^m\frac{m_j}{z-\alpha_j}+H(z),
\tag{18}
\]

with `H` holomorphic on `|z|<R`. Comparing coefficients in `(12)` gives

\[
\lambda_n
=
-\sum_{j=1}^m m_j\alpha_j^{-n}
+h_{n-1}.
\tag{19}
\]

Cauchy estimates on any intermediate radius show that the remainder has root rate strictly smaller than

\[
q:=r_0^{-1}>1.
\tag{20}
\]

Writing `\alpha_j=r_0\omega_j` with `|\omega_j|=1`, equation `(19)` has exactly the form `(1)`--`(3)`, with distinct unit phases `u_j=\omega_j^{-1}` and nonzero coefficients `c_j=-m_j`. Therefore every thick `S` satisfies

\[
\limsup_{\substack{n\to\infty\\n\in S}}|\lambda_n|^{1/n}=r_0^{-1}>1
\tag{21}
\]

when RH is false.

If RH is true, `(15)` puts all zero-generated singularities on the unit circle, so `G` is holomorphic on `|z|<1`. Cauchy--Hadamard applied to `(12)` yields

\[
\limsup_{n\to\infty}|\lambda_n|^{1/n}\le1,
\tag{22}
\]

and every subsequence, hence every thick subsequence, inherits the same upper bound. Combining `(21)` and `(22)` proves `(5)`.

### 3. A thick set may have density zero

For the explicit set `(6)`, the `k`th retained block has length `k`, so arbitrarily long consecutive intervals occur. Up to the start of the `K`th block, the total number of retained indices is at most

\[
1+2+\cdots+K=O(K^2),
\tag{23}
\]

whereas the ambient scale is `2^{K^2}`. Inside the next short block the numerator changes by only `O(K)`. Consequently

\[
\frac{|S\cap[1,N]|}{N}\longrightarrow0.
\tag{24}
\]

Thus `(5)` can be certified from an asymptotically zero fraction of the Li output coordinates.

## Prior-art audit

The Li/Keiper generating-function framework and the RH/off-RH exponential asymptotics are classical. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, analyzes the conformal map `z=1-1/s`, the transformed zero singularities, and the resulting exponential oscillatory behavior when RH fails. Keiper's original power-series treatment and later Li-coefficient literature are already recorded in `research/arithmetic_fidelity/SOURCES.md`.

The finite-window argument `(7)`--`(9)` is elementary Vandermonde linear algebra and belongs to the classical finite-exponential/Prony observability picture. No novelty is claimed for that lemma in isolation.

A targeted literature search for Li criteria stated on arbitrary thick subsequences, zero-density thick subsets, sparse Li root-rate criteria, and closely equivalent subsequence formulations did not locate the exact statement `(5)`--`(6)`. This is not an exhaustive novelty proof. The `CANDIDATE-NEW-STRUCTURE` label applies narrowly to the synthesis: **finite-mode local observability, rather than output density, is sufficient to preserve the Li off-critical root discriminator even on a density-zero retained set**.

## Boundaries / caveats

**Output compression only.** The theorem assumes the selected `\lambda_n` have already been formed. Computing a large `\lambda_n` from the local Taylor/source data of `\xi'/\xi` can still require source depth proportional to `n` and cancellation across that depth, as AF-238--AF-243 show. Sparse output storage or observation is therefore not sparse source access.

**Thickness is sufficient, not shown necessary.** Many much sparser or more irregular sets may still observe every finite exponential mode. AF-244 does not characterize the minimal sampling condition. The natural next object is the class of subsets `S` that are uniqueness/observability sets for every finite unit-circle exponential polynomial.

**No positivity information.** The criterion uses `|\lambda_n|^{1/n}` and retains only the exponential root discriminator. It does not preserve the Li positivity criterion term by term, nor does it identify signs, phases, individual zeros, or multiplicities beyond what is encoded in the dominant root rate.

**No computational-efficiency claim.** Density-zero output sampling does not imply a density-zero arithmetic workload because each selected high-index coefficient may still be expensive in source information.

**Finite dominant mode is essential to this proof.** The uniform finite-window lower bound follows from a fixed finite Vandermonde system. Extending the argument to infinitely many co-dominant modes, continuous spectral mass, or moving mode families requires a different observability theorem.

**Harmless indexing conventions.** Some literature indexes the derivative generating series as `\sum_{n\ge0}\lambda_{n+1}z^n`; `(12)` is the same convention with the index shifted. Such a finite shift does not affect any root-rate or thickness conclusion.

## Consequence

The next Arithmetic Fidelity question is no longer simply “how many outputs must survive?” For finite exponential discriminators it is more precise to ask:

> Which sampling geometries are recurrence-determining or uniformly observable for the relevant mode class?

Thickness is a strong sufficient condition and density is demonstrably unnecessary. A sharper theory should classify weaker retained sets through generalized Vandermonde frames, recurrence/uniqueness properties, or quantitative observability constants, then ask which of those properties survive when the dominant structure is no longer a fixed finite exponential polynomial.

For the Li program specifically, this creates a clean separation of compression axes: **source-access compression remains hard, while output-index compression can be extreme without losing the RH root-rate discriminator**. Any future claim about the “information price” of Li-based detection should specify which of those two axes it is measuring.