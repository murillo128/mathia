# PC-412 — cross-frequency LCM descendants are a universal zeta dephasing kernel

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-REFORMULATION` + `DECISIVE-NEGATIVE` for the most direct different-Mellin-frequency escape left open by PC-410/PC-411. If two distinct descendant labels are coupled only through the reciprocal common refinement `[m,k]^{-s}`, then allowing different Mellin frequencies `t` and `u` does restore every fresh-prime direction that cancels on the Mellin diagonal. However, the restored all-prime factor is exactly the universal shifted-zeta ratio `zeta(s-i(t-u))/zeta(s)`, while the parent shell contributes only finitely many Euler factors. For real `s>1` the universal factor is the characteristic function of the classical zeta distribution on logarithmic dilations. The same kernel acts on every arbitrary matched base profile propagated by the universal descendant semigroup, so this off-diagonal frequency coherence is not a retained Prime-Circle geometric carrier.

This does **not** classify arbitrary two-label kernels, source-dependent angular/chord/old-new refinement couplings, non-join dependence, nonlinear state-space changes, or interaction complexity growing with conductor. It closes the canonical cross-frequency continuation of the reciprocal-LCM/join-only branch and gives the exact fresh-prime response for an arbitrary join-shell weight.

## 1. Off-diagonal descendant symbol

Keep the shell-2 descendant multipliers from PC-405--PC-411. For a fixed parent shell `n`, real Mellin frequency `t`, and descendant label `m`,

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\]

with prime-power factors

\[
c_{n,p^a}(t)=
\begin{cases}
1,&a=0,\\[1mm]
p^{iat},&a\ge1,\ p\mid n,\\[1mm]
p^{iat}-p^{i(a-1)t},&a\ge1,\ p\nmid n.
\end{cases}
\tag{1}
\]

PC-410 proves that a join-only coupling deletes every positive fresh-prime max shell when the two Mellin frequencies are the same. Its explicit surviving boundary was to mix different frequencies. Test that boundary directly by defining, initially for `Re(s)>1`,

\[
\boxed{
K_n(s;t,u)
:=
\sum_{m,k\ge1}
\frac{c_{n,m}(t)\overline{c_{n,k}(u)}}{[m,k]^s}.
}
\tag{2}
\]

For fixed real `t,u`, absolute convergence in this half-plane follows Euler-locally from geometric prime-power tails and globally from local factors `1+O(p^{-Re(s)})`. Equation (2) is an off-diagonal Mellin kernel, not a new Hilbert-space spectral operator by itself.

## 2. Fresh-prime max shells no longer cancel, but their residue is universal

Fix a fresh prime `p\nmid n` and write

\[
A=p^{it},\qquad C=p^{-iu},\qquad D=AC=p^{i(t-u)}.
\tag{3}
\]

The two local descendant sequences are

\[
e_0=1,\qquad e_a=A^a-A^{a-1}\quad(a\ge1),
\]

and

\[
f_0=1,\qquad f_b=C^b-C^{b-1}\quad(b\ge1).
\tag{4}
\]

Their cumulative sums telescope separately:

\[
E_r:=\sum_{a=0}^r e_a=A^r,
\qquad
F_r:=\sum_{b=0}^r f_b=C^r.
\tag{5}
\]

Therefore the total coefficient carried by the positive max shell `max(a,b)=r` is exactly

\[
\begin{aligned}
\sum_{\max(a,b)=r}e_af_b
&=E_rF_r-E_{r-1}F_{r-1}\\
&=D^r-D^{r-1},\qquad r\ge1.
\end{aligned}
\tag{6}
\]

This is the precise off-diagonal replacement for the PC-410 cancellation. At `t=u`, `D=1` and every positive max shell vanishes. At `t\ne u`, the shell survives, but its entire dependence is the one-dimensional geometric character `D^r`.

More generally, if a fresh-prime join-only kernel assigns an arbitrary local weight `omega_r` to max shell `r`, then its local response is

\[
\boxed{
\omega_0+(D-1)\sum_{r\ge1}D^{r-1}\omega_r.
}
\tag{7}
\]

Thus frequency mixing breaks the diagonal cancellation without creating a new multidimensional fresh-prime datum: the whole max-shell packet is compressed to a universal geometric finite-difference transform depending only on `p^{i(t-u)}`.

## 3. Reciprocal LCM gives an exact shifted-zeta ratio

For the canonical reciprocal-refinement kernel of PC-409, put

\[
x=p^{-s},\qquad \omega_r=x^r.
\tag{8}
\]

Substituting (8) into (6) gives the exact fresh-prime local factor

\[
\begin{aligned}
F_p(s;t,u)
&=1+\sum_{r\ge1}(D^r-D^{r-1})x^r\\
&=\boxed{\frac{1-x}{1-Dx}}\\[1mm]
&=\boxed{\frac{1-p^{-s}}{1-p^{-s+i(t-u)}}}.
\end{aligned}
\tag{9}
\]

Multiplying (9) over fresh primes already identifies the infinite all-prime part. If every prime were fresh, then

\[
\boxed{
\prod_pF_p(s;t,u)
=
\frac{\zeta(s-i(t-u))}{\zeta(s)},
\qquad \Re(s)>1.
}
\tag{10}
\]

The ratio is therefore not produced by a new source-specific interaction between two descendants. It is forced by the universal fresh-prime difference law together with the max/join weight.

## 4. Parent primes give only a finite correction

At a repeated parent prime `p\mid n`, there is no fresh-prime difference. The two local sequences are simply `A^a` and `C^b`. Hence

\[
G_p(s;t,u)
:=
\sum_{a,b\ge0}A^aC^b x^{\max(a,b)}.
\tag{11}
\]

Summing by max shells, or equivalently using the cumulative geometric sums, gives

\[
\boxed{
G_p(s;t,u)
=
\frac{1-Dx^2}
{(1-Ax)(1-Cx)(1-Dx)}.
}
\tag{12}
\]

Relative to the universal fresh factor (9), the parent-prime correction is

\[
\boxed{
\frac{G_p}{F_p}
=
\frac{1-Dx^2}
{(1-Ax)(1-Cx)(1-x)}.
}
\tag{13}
\]

Combining (10)--(13) yields the full exact factorization

\[
\boxed{
K_n(s;t,u)
=
\frac{\zeta(s-i(t-u))}{\zeta(s)}
\prod_{p\mid n}
\frac{1-p^{-2s+i(t-u)}}
{(1-p^{-s+it})(1-p^{-s-iu})(1-p^{-s})},
\qquad \Re(s)>1.
}
\tag{14}
\]

All dependence on the parent shell is confined to the finite product over `p\mid n`. The only infinite fresh-prime factor is the universal ratio in (10).

The diagonal limit is an exact consistency check. Setting `u=t` makes the zeta ratio equal to `1`, and each parent factor becomes

\[
\frac{1-p^{-2s}}
{(1-p^{-s+it})(1-p^{-s-it})(1-p^{-s})}
=
\frac{1+p^{-s}}
{(1-p^{-s+it})(1-p^{-s-it})},
\tag{15}
\]

which is exactly the repeated-parent factor of PC-409. Thus PC-409 is recovered without a limiting argument.

## 5. The fresh-prime kernel is the classical zeta-distribution characteristic function

For real `sigma>1`, define

\[
Z_\sigma(\delta)
:=
\frac{\zeta(\sigma-i\delta)}{\zeta(\sigma)}.
\tag{16}
\]

Its Dirichlet series is

\[
\boxed{
Z_\sigma(\delta)
=
\sum_{r\ge1}
\frac{r^{-\sigma}}{\zeta(\sigma)}e^{i\delta\log r}.
}
\tag{17}
\]

Therefore `Z_sigma` is the characteristic function of the random logarithmic dilation `Y=log N` when

\[
\Pr(N=r)=\frac{r^{-\sigma}}{\zeta(\sigma)}.
\tag{18}
\]

This is the classical zeta distribution. In particular, `Z_sigma(t-u)` is a translation-invariant positive-definite kernel in Mellin frequency, satisfies `|Z_sigma(t-u)|<=1`, and equals `1` on the diagonal. Takashi Nakamura's 2022 work on zeta distributions generated by Dirichlet series uses the standard characteristic-function form `Z(sigma+it)/Z(sigma)`; (16) is the same object up to the Fourier-sign convention (arXiv:2209.13257).

For the descendant problem this has a direct representation-theoretic meaning. The fresh-prime refinement layer acts on off-diagonal Mellin coherence by the universal random-dilation/dephasing kernel `Z_sigma(t-u)`. It averages phases according to a source-independent zeta distribution; it does not manufacture a new Prime-Circle-specific frequency coupling.

## 6. Matched arbitrary-profile control

Let `h` be any Mellin-tame nonarithmetic base profile and propagate it with the same source-independent descendant operators used in PC-405--PC-411. Its off-diagonal descendant coherence is

\[
\widehat h(t)\overline{\widehat h(u)}K_n(s;t,u).
\tag{19}
\]

Every factor in (14) is unchanged. Replacing the genuine cyclotomic shell profile by an arbitrary matched profile changes only the base coherence `hat h(t) overline{hat h(u)}`; the shifted-zeta factor, the fresh-prime response, and the finite parent correction are identical.

This matched control is decisive for the Prime-Circle objective. Different Mellin frequencies genuinely retain more information than the diagonal PC-410 calculation, but the newly retained information comes from the universal descendant/refinement representation itself. It is not evidence that the original roots-of-unity geometry generated an additional arithmetic carrier.

## 7. Prior-art and novelty audit

The analytic factor in (10) is classical from two independent directions. First, PC-408 already obtains `zeta(s-it)/zeta(s)` as the degree-one conductor symbol of the same universal fresh-prime descendant law. PC-412 shows that distinct-index frequency mixing does not escape that package: it reproduces the same ratio with `t` replaced by the frequency difference `t-u`.

Second, for real `s>1`, the probabilistic interpretation (17)--(18) is standard zeta-distribution theory; the characteristic-function ratio is explicitly part of the literature on zeta distributions generated by Dirichlet series. The reciprocal-LCM kernel itself also remains inside the classical GCD/LCM meet-join territory already anchored in `SOURCES.md` and audited in PC-409--PC-411.

The project-local contribution is therefore the exact off-diagonal classification (6), (9), and (14): the specific escape explicitly left open by the previous join-only no-go does survive algebraically, but its surviving all-prime coherence classicalizes immediately to a universal shifted-zeta characteristic kernel. No historical novelty is claimed for the zeta ratio, zeta distribution, or LCM technology.

Nothing in (14) supplies a new gamma factor, an intrinsic `s<->1-s` symmetry, or a critical-line selector. Meromorphically continuing the displayed zeta ratio outside the native absolute-convergence region does not turn its inherited zeros or poles into new spectral data of the original Prime-Circle geometry.

## 8. Falsification, checks, and remaining boundary

The local formulas can be attacked independently of any global Euler product. For a fresh prime, direct truncation of

\[
\sum_{0\le a,b\le R}e_af_bx^{\max(a,b)}
\]

must converge to (9); for a parent prime, the analogous repeated sequence must converge to (12). As a numerical stress test at `s=2.3`, `t=0.7`, `u=-0.2`, truncation at exponent `R=30` for `p=2,3,5,7` agrees with (9) and (12) to about `3e-15` or better. The diagonal specialization must recover (15) exactly.

The obstruction has a sharp boundary. Equation (7) shows that **join-shell dependence plus cross-frequency mixing** still exposes only a one-dimensional geometric character at each fresh prime. Equation (14) closes the canonical multiplicative reciprocal-LCM realization of that branch completely. It does not rule out a genuinely two-label kernel that is not a function of the join alone, a source-dependent kernel coupled to angular/chord/old-new data before Mellin diagonalization, nonlinear descendant interactions, or complexity that grows with conductor.

The surviving research requirement is therefore stricter than merely `t\ne u`. A successful distinct-descendant mechanism must retain source-selected information that cannot be reproduced by the universal dilation/difference semigroup acting on an arbitrary matched base profile.
