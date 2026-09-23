# PC-407 — shell-2 quadratic descendant energy is generalized-Jordan data

**Status:** `EXACT-DERIVED` + `CLASSICAL-REFORMULATION` + `DECISIVE-NEGATIVE` for the canonical positive quadratic/nonlinear completion left open by PC-406. The full shell-2 descendant family admits a natural `L^2` energy after the canonical dilation conjugacy. Its conductor-generating multiplier is exactly the Dirichlet series of the squared modulus of a generalized Jordan totient of imaginary order. It factors as a shifted-zeta quotient times an Euler product already absolutely convergent for `Re(s)>1/2`. This produces an exact RH-equivalent pole criterion, but the criterion lives entirely in the universal dilation semigroup and is reproduced by every matched nonarithmetic base profile. Thus the apparently stronger nonlinear/RH-sensitive object does not recover cyclotomic geometry lost by PC-405/PC-406.

This does **not** rule out nonlinear couplings that mix different descendants before the universal dilation reduction, couple shell-2 radial data to independent angular/chord/old-new information, or introduce a genuinely source-dependent product law. It closes the ordinary Hilbert-norm square of each descendant followed by the canonical conductor Dirichlet sum, together with its polarized quadratic form and frequency-resolved Mellin symbol.

## 1. Put the PC-405 descendant law in its unitary Hilbert representation

PC-406 identifies the canonically conjugated shell-2 measure with the PC-179 signed radial-flux measure,

\[
d\nu_n(x)=\rho_n(x)\,dx,
\qquad
\rho_n(x)=-\frac d{dx}\log\Phi_n(e^{-x}),
\tag{1}
\]

and the prime-child rule is

\[
\nu_{pn}=\begin{cases}
S_p\nu_n,&p\mid n,\\
(S_p-I)\nu_n,&p\nmid n,
\end{cases}
\tag{2}
\]

where `S_a` is pushforward under `x -> x/a`.

For `n>1`, PC-406 notes that `rho_n` is bounded at `0+` and exponentially decaying at infinity. Hence

\[
h_n(x):=x\rho_n(x)
\tag{3}
\]

belongs to

\[
\mathcal H:=L^2(\mathbb R_+,dx/x),
\qquad
d\nu_n(x)=h_n(x)\,\frac{dx}{x}.
\tag{4}
\]

If

\[
(V_a h)(x):=h(ax),
\tag{5}
\]

then `V_a` is unitary on `H`, `V_aV_b=V_{ab}`, and pushforward by `S_a` on measures is exactly `V_a` on their `dx/x` densities. Therefore (2) becomes

\[
\boxed{
h_{pn}=\begin{cases}
V_p h_n,&p\mid n,\\
(V_p-I)h_n,&p\nmid n.
\end{cases}}
\tag{6}
\]

This is the natural Hilbert-space realization of the same source-forced refinement law, with no new operator chosen by hand.

For a prime power in a descendant conductor, the local operators are therefore

\[
C_{n,p^k}=\begin{cases}
V_{p^k},&p\mid n,\\
V_{p^{k-1}}(V_p-I),&p\nmid n,\quad k\ge1,
\end{cases}
\tag{7}
\]

and for `m=prod p^{k_p}`,

\[
h_{nm}=C_{n,m}h_n,
\qquad
C_{n,m}=\prod_p C_{n,p^{k_p}}.
\tag{8}
\]

## 2. Mellin-Plancherel makes the nonlinear norm exactly multiplicative

Use the multiplicative Fourier transform

\[
\widehat h(t)=\int_0^\infty h(x)x^{-it}\,\frac{dx}{x}.
\tag{9}
\]

With this normalization,

\[
\widehat{V_a h}(t)=a^{it}\widehat h(t),
\qquad
\|h\|_{\mathcal H}^2
=\frac1{2\pi}\int_{\mathbb R}|\widehat h(t)|^2\,dt.
\tag{10}
\]

Thus a repeated prime contributes only a phase, while a fresh prime contributes

\[
a_p(t):=|p^{it}-1|^2
=2-p^{it}-p^{-it}
=2-2\cos(t\log p).
\tag{11}
\]

In particular, the exponent of a fresh prime in `m` disappears from the norm. Equations (7)--(10) give the exact identity

\[
\boxed{
\|h_{nm}\|_{\mathcal H}^2
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat h_n(t)|^2
\prod_{\substack{p\mid m\\p\nmid n}}a_p(t)\,dt.
}
\tag{12}
\]

This is genuinely nonlinear in the descendant field: the signed measure has been squared before descendants are summed. It is therefore outside the linear scalarization closed by PC-406.

For the actual Prime-Circle source, (9) is nevertheless old scalar data. Since `h_n=x rho_n`,

\[
\widehat h_n(t)
=
\int_0^\infty \rho_n(x)x^{-it}\,dx
=M_{-it}(\nu_n),
\tag{13}
\]

so PC-406 gives

\[
\widehat h_n(t)
=-\Gamma(1-it)\zeta(1-it)n^{it}
\prod_{p\mid n}(1-p^{-it}).
\tag{14}
\]

The only question is therefore whether squaring descendants and summing over all conductors creates a new interaction in the universal multiplier.

## 3. The full quadratic descendant sum has an exact Euler product

For real `sigma>1`, define the canonical conductor-weighted energy

\[
\mathcal E_n(\sigma)
:=
\sum_{m\ge1}\frac{\|h_{nm}\|_{\mathcal H}^2}{m^\sigma}.
\tag{15}
\]

The sum converges absolutely: `0<=a_p(t)<=4`, so the coefficient in (12) is bounded by `4^{omega(m)}`, whose Dirichlet series converges for `sigma>1`. Tonelli and (12) therefore give

\[
\boxed{
\mathcal E_n(\sigma)
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat h_n(t)|^2\,
\mathcal D_n(\sigma,t)\,dt,
}
\tag{16}
\]

where

\[
\mathcal D_n(s,t)
:=
\sum_{m\ge1}\frac1{m^s}
\prod_{\substack{p\mid m\\p\nmid n}}a_p(t),
\qquad \Re(s)>1.
\tag{17}
\]

This coefficient is multiplicative in `m`. Put `x=p^{-s}`. If `p|n`, the local factor is simply

\[
\sum_{k\ge0}x^k=\frac1{1-x}.
\tag{18}
\]

If `p\nmid n`, every positive exponent carries the same factor `a_p(t)`, so

\[
1+a_p(t)\sum_{k\ge1}x^k
=
\frac{1+\bigl(1-p^{it}-p^{-it}\bigr)x}{1-x}.
\tag{19}
\]

Hence

\[
\boxed{
\mathcal D_n(s,t)
=
\prod_{p\mid n}(1-p^{-s})^{-1}
\prod_{p\nmid n}
\frac{1+(1-p^{it}-p^{-it})p^{-s}}{1-p^{-s}}.
}
\tag{20}
\]

No approximation has entered: (20) is the exact Mellin-frequency symbol of the full quadratic descendant energy.

## 4. The arithmetic coefficient is the squared modulus of a generalized Jordan totient

For a complex parameter `z`, write the usual generalized Jordan expression

\[
J_z(m):=m^z\prod_{p\mid m}(1-p^{-z}).
\tag{21}
\]

At imaginary order `z=it`, `|m^{it}|=1`, and therefore

\[
\boxed{
|J_{it}(m)|^2
=
\prod_{p\mid m}|1-p^{-it}|^2
=
\prod_{p\mid m}a_p(t).
}
\tag{22}
\]

Consequently the all-fresh version of (17) is exactly

\[
\mathcal D_*(s,t)
:=
\prod_p
\frac{1+(1-p^{it}-p^{-it})p^{-s}}{1-p^{-s}}
=
\sum_{m\ge1}\frac{|J_{it}(m)|^2}{m^s}.
\tag{23}
\]

Primes already dividing the parent only remove their fresh-prime factor:

\[
\boxed{
\mathcal D_n(s,t)
=
\mathcal D_*(s,t)
\prod_{p\mid n}
\bigl[1+(1-p^{it}-p^{-it})p^{-s}\bigr]^{-1}.
}
\tag{24}
\]

Thus the first natural nonlinear completion of the descendant law does not generate a new arithmetic family. It lands in the classical multiplicative-function world of Jordan totients and their products.

## 5. A shifted-zeta factorization exposes an exact but classical RH criterion

The local factor in (23) agrees to first order in `p^{-s}` with a standard shifted-zeta quotient. Define

\[
Q_p(s,t)
:=
\frac{(1-p^{-(s-it)})(1-p^{-(s+it)})}{(1-p^{-s})^2},
\tag{25}
\]

which is the `p`-factor of

\[
\frac{\zeta(s)^2}{\zeta(s-it)\zeta(s+it)}.
\tag{26}
\]

Writing `a_p=a_p(t)`, direct algebra gives

\[
\frac{
\bigl[1+(1-p^{it}-p^{-it})p^{-s}\bigr](1-p^{-s})
}{
(1-p^{-(s-it)})(1-p^{-(s+it)})
}
=
1-
\frac{a_p p^{-2s}}
{(1-p^{-(s-it)})(1-p^{-(s+it)})}.
\tag{27}
\]

Therefore

\[
\boxed{
\mathcal D_*(s,t)
=
\frac{\zeta(s)^2}
{\zeta(s-it)\zeta(s+it)}
\,H(s,t),
}
\tag{28}
\]

where

\[
H(s,t)
:=
\prod_p
\left(
1-
\frac{a_p(t)p^{-2s}}
{(1-p^{-(s-it)})(1-p^{-(s+it)})}
\right).
\tag{29}
\]

The product (29) converges absolutely and locally uniformly for `Re(s)>1/2`: for fixed real `t`, its `p`-factor is `1+O(p^{-2 Re(s)})`, while the denominators in (29) are nonzero because `|p^{-(s+-it)}|=p^{-Re(s)}<1`. Hence (28) meromorphically continues the frequency-resolved multiplier from `Re(s)>1` into `Re(s)>1/2`.

On the real axis `s=sigma>1/2`, every local factor of the original Euler product (23) is positive, `Q_p(sigma,t)>0`, and hence `H(sigma,t)>0`. Likewise each finite correction in (24) is positive because

\[
1+(a_p(t)-1)p^{-\sigma}\ge 1-p^{-\sigma}>0.
\tag{30}
\]

There can therefore be no cancellation of shifted-zeta zeros on the real interval `(1/2,1)`. If `rho=beta+i gamma` is a nontrivial zeta zero with `beta>1/2`, then at `t=gamma` the continuation of `D_n(s,t)` has a pole at the real point `s=beta`. Conversely, any such shifted-zeta pole there comes from a zero of `zeta(beta+i t)`. By the functional-equation symmetry of the nontrivial zeros,

\[
\boxed{
\mathrm{RH}
\iff
\text{for every real }t,
\ \mathcal D_n(s,t)
\text{ has no pole at any real }s\in(1/2,1),
}
\tag{31}
\]

for any fixed parent `n>1`. The pole at `s=1` for generic `t` is the ordinary positive-coefficient divergence and is not part of (31).

Equation (31) looks at first like precisely the kind of critical-half-plane signal sought by the Prime-Circle program. The novelty/falsification checks below show why it is not a new Prime-Circle RH mechanism.

## 6. The matched arbitrary-profile control reproduces the entire RH-sensitive multiplier

Take an arbitrary `h in L^2(R_+,dx/x)` and declare synthetic descendants using exactly the source-derived operators (7), without requiring `h` to come from a cyclotomic shell. Every step from (9) through (31) remains unchanged. The base profile enters only through `|hat h(t)|^2` in (16); the multiplier `D_n(s,t)`, its generalized-Jordan coefficients, the `Re(s)=1/2` continuation threshold, and the RH-equivalent shifted-zeta pole criterion are all independent of the cyclotomic source.

This is the decisive falsification control. The apparent critical-line bridge is carried by the universal dilation/difference semigroup after PC-405's conjugacy, not by roots-of-unity geometry retained in the shell profile. Any nonarithmetic base profile propagated by the same prime-indexed dilation rule inherits exactly the same criterion.

The actual Prime-Circle source contributes (14), which is already the one-shell Mellin factor classified in PC-179/PC-406. The quadratic descendant assembly therefore combines two separately known pieces: an old cyclotomic Mellin profile and a universal generalized-Jordan multiplier. It does not create a new interaction between them.

Polarization does not repair this. Replacing `||C_{n,m}h||^2` by

\[
\langle C_{n,m}h,C_{n,m}g\rangle
\tag{32}
\]

for two arbitrary base profiles simply replaces `|hat h(t)|^2` in (16) by `hat h(t) overline{hat g(t)}` while leaving the same multiplier (20). Thus the complete quadratic Gram form of the descendant orbit is still a universal Mellin multiplier acting on base-profile spectral data.

## 7. Prior-art and novelty audit

The arithmetic ingredients are classical. Jordan's totient has the standard product

\[
J_k(m)=m^k\prod_{p\mid m}(1-p^{-k})
\tag{33}
\]

and standard Dirichlet generating function `zeta(s-k)/zeta(s)`; PC-406 already used the same complex-parameter extension in its linear descendant calculation. R. Sivaramakrishnan's *Classical Theory of Arithmetic Functions* (CRC Press, 1988/1989, Section V.3) is a standard reference for the Jordan product structure. Chandran and Namboothiri, *Two identities involving Cohen-Ramanujan expansions* (arXiv:2503.12027, 2025), explicitly place Jordan totients and correlations/products of normalized Jordan functions inside established Ramanujan-Fourier arithmetic.

The new local calculation (23)--(29) is elementary multiplicative-function algebra rather than a new zeta identity: `|J_it(m)|^2` is multiplicative, so its Dirichlet series has (19) as its Euler factor, and extracting the two shifted linear terms necessarily produces `zeta(s)^2/[zeta(s-it)zeta(s+it)]` with a second-order convergent remainder. Such shifted-zeta factorizations are standard analytic-number-theory behavior for products/second moments of multiplicative functions. Mellin-Plancherel diagonalization of `V_a` is likewise ordinary harmonic analysis on the multiplicative half-line.

The RH statement (31) is therefore a reformulation of the zero set already exposed explicitly in the denominator of (28), not an independent spectral theorem. In particular, the half-plane `Re(s)>1/2` appears because the first-order Euler terms have been extracted and the residual Euler product begins at `p^{-2s}`. No source-derived self-adjoint operator, functional-equation involution, positivity theorem forcing `beta=1/2`, or new zero constraint is produced.

No historical novelty is claimed for the generalized-Jordan, Mellin, shifted-zeta, or RH-equivalence pieces. The durable project-local result is the exact identification of the canonical shell-2 quadratic descendant observable with that classical package, including the matched-control proof that its apparently promising RH sensitivity is universal rather than cyclotomic.

## 8. Falsification checks and surviving frontier

Several exact checks constrain the derivation. At `t=0`, every fresh-prime multiplier vanishes, so (20) reduces to

\[
\mathcal D_n(s,0)=\prod_{p\mid n}(1-p^{-s})^{-1},
\tag{34}
\]

exactly as (6) predicts because `(V_p-I)` kills the zero Mellin frequency. A repeated prime contributes a unitary phase for every exponent and hence the geometric factor `(1-p^{-s})^{-1}`. For a fresh prime, both `p` and `p^k` have the same norm multiplier `a_p(t)`, reproducing the local series (19). Expanding finitely many Euler factors coefficient-by-coefficient agrees with the direct multiplicative coefficient in (17).

The branch closed here is therefore precise:

\[
\text{shell-2 descendant dilation orbit}
\longrightarrow
\text{ordinary }L^2\text{ norm/polarized quadratic form}
\longrightarrow
\text{conductor Dirichlet sum}
\longrightarrow
\text{generalized-Jordan shifted-zeta package}.
\]

What remains outside the no-go is equally precise. A surviving nonlinear mechanism must use information not determined by a single base profile plus the universal commuting dilations: for example a source-forced interaction between distinct descendant levels before separate Mellin diagonalization, an independent angular/chord/old-new variable coupled to the radial refinement, a genuinely noncommutative or non-functorial cross-level product, or an infinite-depth renormalization whose operation is not reducible to a quadratic form of the dilation orbit. Such a candidate must again beat the matched arbitrary-profile control.

## Consequence

The most natural positive quadratic escape from PC-406 is exhausted. Squaring descendant fields before the conductor sum does create a frequency-resolved object whose analytic continuation detects off-critical zeta zeros exactly, but this apparent success is deceptive: the multiplier is the classical Dirichlet series of `|J_it(m)|^2`, and the same RH-equivalent pole criterion is present for every arbitrary base profile subjected to the universal PC-405 dilation rule. Prime Circle contributes no additional constraint on the zeros. Further progress must introduce a source-specific interaction law before this universal dilation/Mellin collapse, rather than another norm, polarization, or Euler-product resummation of the same descendant orbit.
