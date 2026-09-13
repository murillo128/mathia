# PC-282 — boundary-first radial logarithmic operator collapses to the exact selector

**Status:** `DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the unsmoothed-logarithm escape left open by PC-281.

PC-281 closes the regular or sufficiently mollified side of the PC-280 finite-section family, but deliberately leaves the actual logarithmic singularity at the common vertex outside its Lipschitz transport theorem. The most direct way to approach that singularity is from the harmonic interior. Let `q` be an odd prime, let

\[
H_B:=\{-B,\ldots,B\},\qquad N:=2B+1\le q,
\]

and take source units `p,r in (Z/qZ)^*`. For `0<rho<1`, define the intrinsic radial logarithmic profile

\[
f_\rho(t):=\log|1-\rho\zeta_q^t|,
\qquad \zeta_q=e^{2\pi i/q},
\tag{1}
\]

and its PC-280 finite section

\[
L_{p,r;B}^{(\rho)}(h,k)
:=f_\rho(ph+rk),
\qquad h,k\in H_B.
\tag{2}
\]

Put

\[
a_\rho:=-\log(1-\rho)>0
\tag{3}
\]

and let the exact collision selector be

\[
Z_{p,r;B}(h,k)
:=\mathbf 1_{\{ph+rk\equiv0\pmod q\}}.
\tag{4}
\]

Then the boundary singularity has a rigid leading operator:

\[
\boxed{
\frac{L_{p,r;B}^{(\rho)}}{a_\rho}
\longrightarrow
-Z_{p,r;B}
\quad\text{in operator norm as }\rho\uparrow1
}
\tag{5}
\]

for every fixed `(q,B,p,r)`. More quantitatively, for `rho>=1/2`,

\[
\boxed{
\left\|
\frac{L_{p,r;B}^{(\rho)}}{a_\rho}+Z_{p,r;B}
\right\|_{\rm op}
\le
\frac{N C_q}{a_\rho},
\qquad
C_q:=\log2+\log\csc(\pi/q)=O(\log q).
}
\tag{6}
\]

Consequently the same collapse holds uniformly in every simultaneous regime satisfying

\[
\frac{a_\rho}{N\log q}\longrightarrow\infty.
\tag{7}
\]

This is stronger than a statement about one scalar statistic. The **entire leading matrix** becomes the exact PC-280 selector, and hence all normalized singular values do as well. Because that selector is determined solely by the source quotient `p r^{-1} mod q`, its prime-source arithmetic lies inside the exact ratio-statistic framework already classicalized by PC-272.

Thus taking the harmonic logarithm to the boundary first, or entering the explicit ultra-singular sector (7), does **not** rescue a new RH-facing carrier from the common-vertex singularity. The unresolved part is the genuinely coupled transition regime in which neither PC-281 regular-profile transport nor the selector-dominance estimate (6) is small, or a renormalized construction that subtracts the divergent selector and proves new information in the remainder.

## 1. Exact singular/regular decomposition

At the resonant residue `t=0`,

\[
f_\rho(0)=\log(1-\rho)=-a_\rho.
\tag{8}
\]

Therefore (2) has the exact decomposition

\[
\boxed{
L_{p,r;B}^{(\rho)}
=-a_\rho Z_{p,r;B}+R_{p,r;B}^{(\rho)},
}
\tag{9}
\]

where `R^{(rho)}(h,k)=0` on the collision set and equals `f_rho(ph+rk)` otherwise. For fixed `q` there are only finitely many nonzero residues, and

\[
\log|1-\rho\zeta_q^t|
\longrightarrow
\log|1-\zeta_q^t|
\qquad(t\ne0)
\tag{10}
\]

as `rho -> 1`. Hence `R^{(rho)}` remains bounded entrywise, and therefore in operator norm, while `a_rho -> infinity`. Dividing (9) by `a_rho` proves (5) immediately.

This order-of-limits statement is intrinsic rather than an arbitrary spectral wrapper. The scale `a_rho` is exactly the divergent value of the geometric logarithmic potential at the anchored collision itself.

## 2. Uniform ultra-singular estimate

For every nonzero residue `t` and `rho>=1/2`,

\[
\begin{aligned}
|1-\rho e^{2\pi i t/q}|^2
&=(1-\rho)^2+4\rho\sin^2(\pi t/q)\\
&\ge 2\sin^2(\pi/q),
\end{aligned}
\tag{11}
\]

while trivially `|1-rho e^{2 pi i t/q}|<=2`. Thus

\[
|f_\rho(t)|
\le
C_q:=\log2+\log\csc(\pi/q)
=O(\log q)
\qquad(t\ne0).
\tag{12}
\]

Since `R^{(rho)}` is an `N x N` matrix,

\[
\|R^{(\rho)}\|_{\rm op}
\le
\|R^{(\rho)}\|_F
\le
N C_q.
\tag{13}
\]

Equations (9) and (13) give (6). In particular, if `q,B,rho` vary together and (7) holds, then the normalized **operator itself** converges to `-Z`, not merely its trace, determinant, or spectral edge.

The singular-value consequence follows from the standard coordinatewise perturbation bound

\[
|\sigma_j(A)-\sigma_j(B)|\le\|A-B\|_{\rm op}.
\tag{14}
\]

Therefore

\[
\boxed{
\max_j
\left|
\frac{\sigma_j(L_{p,r;B}^{(\rho)})}{a_\rho}
-
\sigma_j(Z_{p,r;B})
\right|
\le
\frac{N C_q}{a_\rho}.
}
\tag{15}
\]

## 3. The limiting selector is only exact ratio geometry

Because `N<=q`, the representatives in `H_B` are distinct modulo `q`. Since `p` and `r` are units, each row and each column of `Z` contains at most one nonzero entry. Thus `Z` is a partial permutation matrix. Its rank is exactly

\[
\begin{aligned}
m_{p,r;B}
&=|pH_B\cap(-rH_B)|\\
&=|pH_B\cap rH_B|\\
&=|(pr^{-1})H_B\cap H_B|,
\end{aligned}
\tag{16}
\]

where the middle equality uses `H_B=-H_B`. Hence

\[
\boxed{
\operatorname{SingSpec}(Z_{p,r;B})
=(\underbrace{1,\ldots,1}_{m_{p,r;B}},
\underbrace{0,\ldots,0}_{N-m_{p,r;B}}).
}
\tag{17}
\]

More importantly, even before taking singular values the full support pattern satisfies

\[
Z_{p,r;B}(h,k)
=\mathbf 1_{\{(pr^{-1})h+k\equiv0\pmod q\}},
\tag{18}
\]

so its source dependence factors exactly through the quotient `a=pr^{-1}`. PC-272 already identifies exact prime-source quotient statistics with finite-group prime-character autocorrelations. Any statistic subsequently applied to the leading selector is therefore a function of that same exact quotient variable; the boundary singularity has not produced an independent arithmetic coordinate.

For the singular spectrum specifically, (17) reduces even further to the window-overlap count already exposed by the exact selector control in PC-280.

## 4. Relation to PC-280 and PC-281

PC-280 says that every one-phase finite section has the cyclic-convolution form, but it does not by itself decide whether a sharp profile can retain useful source information. PC-281 then proves that bounded sufficiently regular profiles are transported to the Li-grid control at the level of the complete normalized singular spectrum. The genuine logarithm is absent from that theorem because its boundary Lipschitz scale diverges.

PC-282 closes the opposite, boundary-first end of that gap. As the harmonic regularization reaches the common vertex, the divergence is concentrated **exactly** on the modular collision set, so the leading operator ceases to probe the detailed log-chord field and becomes the discontinuous selector that PC-280 already isolated. The regular and ultra-singular sides therefore fail for different reasons:

- on the regular side, source motion is smooth enough for PC-277/281 Li-grid transport;
- on the ultra-singular side, the anchored divergence overwhelms the remainder and leaves only the classical exact-ratio selector.

This does not make the two regimes meet. The estimate (6) is useful when `a_rho >> N log q`, whereas PC-281 controls regimes through its separate `B L_q` condition. A coupled scaling between those sufficient regions remains a legitimate research target.

## 5. Prior-art and novelty audit

The analytic ingredients in the proof are classical. The radial field `log|1-rho e^{i theta}|` is standard harmonic/logarithmic-potential theory on the disk (equivalently obtainable from the usual Poisson/Fourier machinery), and (14) is the standard Weyl/Mirsky singular-value perturbation bound. Targeted checks against logarithmic-potential transforms, roots-of-unity/log-sine matrices, finite sections, and singular-value perturbation theory found the expected classical surrounding machinery but no reason to treat any of these ingredients as new.

No literature-novelty claim is made. The project-local result is the order-of-limits synthesis forced by the Prime-Circle frontier: the previously surviving unsmoothed anchored logarithm has an exact divergent coefficient supported on the PC-280 modular collision selector, and that coefficient dominates the full operator in (5)--(7). The proof is self-contained and the external facts used are standard; no new load-bearing `SOURCES.md` dependency is required.

The result is also deliberately narrower than a theorem about all logarithmic finite-section asymptotics. It does not assert that the finite remainder in (9), the spectrum after subtracting `-a_rho Z`, or every simultaneous `q,B,rho` scaling is classical. Those are precisely the falsification boundaries of the present no-go.

## 6. Surviving boundary and decisive tests

A candidate that survives PC-282 must avoid confusing the divergent collision coefficient with new arithmetic information. Three concrete routes remain inside the current mandate:

- **renormalized remainder:** subtract `-a_rho Z` before taking spectral/nonlocal observables and demonstrate an order-one discriminator in `R^{(rho)}` that survives matched non-prime controls;
- **intermediate coupled scaling:** choose `q,B,rho` so neither the PC-281 regular transport error nor `N C_q/a_rho` vanishes, then identify a stable limit not reducible to denominator-`q` rational geometry;
- **non-single-profile coupling:** retain cross-level or additional coordinates before the PC-280 one-phase reduction.

The theorem itself is directly falsifiable. Equation (9) is entrywise exact. For every `rho>=1/2`, any example violating the deterministic norm bound (6) falsifies the quantitative claim. For fixed `q,B,p,r`, failure of `L^{(rho)}/a_rho` to converge to `-Z` falsifies (5). Small-prime numerical checks agree with (5) and (15), but no numerical evidence is needed for the stored result.

## 7. Consequence for the research line

The phrase "use the unsmoothed logarithmic singularity" is no longer by itself an escape from the regular-profile no-go of PC-281. In the natural harmonic boundary limit, the singular part is an exact modular collision projector whose complete leading source dependence is only the quotient `pr^{-1}`. At fixed denominator, and uniformly in the explicit sector (7), the full normalized operator and singular spectrum therefore collapse to a structure already reduced by PC-272/280 to classical finite-group/ratio arithmetic.

The remaining logarithmic question is sharper: **does the finite or critically scaled part left after removing the exact selector divergence carry information that matched rational controls cannot reproduce?** Until such a remainder is isolated and survives that comparison, the common-vertex logarithmic blow-up should be treated as a classical selector effect rather than an RH mechanism.
