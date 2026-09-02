# MC-012 — Pintz Section 7 has a repairable parameter/window mismatch

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `PARTIAL-AUDIT`.

## Claim

A direct continuation of the audit of Pintz's recent preprint `MC-S19` finds a third concrete proof-presentation gap in the difficult `vartheta=1` branch behind `MC-009`, distinct from the endpoint issue in `MC-010` and the kernel-height issue in `MC-011`.

In Section 7, equations (7.1)–(7.7) derive an upper cap for `|M(x)|/Z_0(x)` on the interval

\[
x\in [Y^{1-\varepsilon'},Y].
\tag{1}
\]

The paper then chooses

\[
\varepsilon'=\varepsilon/9
\tag{2}
\]

in order to write the cap as

\[
\frac{|M(x)|}{Z_0(x)}\ll e^{\varepsilon\omega(Y)}.
\tag{3}
\]

However, the very next equation (7.8) applies that cap starting at

\[
Y^{1-\varepsilon/8}.
\tag{4}
\]

Since

\[
Y^{1-\varepsilon/8}<Y^{1-\varepsilon/9},
\]

(3), as derived with (2), does not cover the initial slice

\[
[Y^{1-\varepsilon/8},Y^{1-\varepsilon/9}).
\]

This is a genuine parameter/window mismatch in the printed proof.

The mismatch is repairable without weakening the asymptotic conclusion. Keep instead

\[
\boxed{\varepsilon'=\varepsilon/8}
\tag{5}
\]

through the Section 7 upper-bound argument. Then (7.7) gives the slightly looser but fully sufficient cap

\[
\boxed{
|M(x)|\ll Z_0(x)e^{(9/8)\varepsilon\omega(Y)}
\qquad
(Y^{1-\varepsilon/8}\le x\le Y).}
\tag{6}
\]

All subsequent extremal/cutoff estimates survive this constant change. With `kappa=sqrt(epsilon)`, the cutoff still satisfies

\[
\frac{Y}{Y^*}\ll_\varepsilon
\exp\!\bigl(\varepsilon^{1/5}\omega(Y)\bigr)
\tag{7}
\]

for sufficiently small fixed `epsilon` and sufficiently large `Y`, after harmlessly enlarging thresholds/constants. Consequently the final Section 7 lower bound retains the same asymptotic form

\[
D_M(Y)\gg_\varepsilon
Z(Y)\exp\!\bigl(-C\varepsilon^{1/5}\omega(Y)\bigr),
\tag{8}
\]

with an absolute constant `C`; since `epsilon` is arbitrary, this still gives the logarithmic equivalence required by Pintz's Theorem 2.2.

There is also a cleaner way to justify the cutoff step than the asymptotic notation printed in (7.11): retaining the lower endpoint exactly already yields the needed upper bound for `Y/Y^*`, and the later omission of the lower-end contribution follows a posteriori from `omega(Y)=o(log Y)`. Thus the Section 7 assembly survives both the window mismatch and the lower-end bookkeeping.

This materially strengthens the audit chain supporting `MC-009`, but it still does **not** independently verify the whole preprint. In particular, the Section 5 upper bound (5.9), which Section 7 uses as an input, rests on the earlier contour/nonvanishing machinery and has not been reconstructed end-to-end here. `MC-009` therefore remains `NEEDS-AUDIT`.

## 1. Exact location of the mismatch

Let

\[
\rho_0=1-\eta_0+i\gamma_0
\]

be the zero attaining `Z(Y)`, and write

\[
Z_0(x)=\frac{x^{1-\eta_0}}{\gamma_0}.
\]

For `x` in (1), Pintz compares the zero attaining `Z(x)` with `rho_0` and obtains

\[
\frac{Z(x)}{Z_0(x)}\le e^{2\varepsilon'\omega(x)}.
\tag{9}
\]

Applying the Section 5 upper estimate (5.9) with parameter `epsilon'` then gives the displayed bound (7.7)

\[
\frac{|M(x)|}{Z_0(x)}
\ll e^{9\varepsilon'\omega(x)}
\le e^{9\varepsilon'\omega(Y)}.
\tag{10}
\]

The paper chooses `epsilon'=epsilon/9`, so (10) becomes (3), but its derivation is still restricted to

\[
x\ge Y^{1-\varepsilon/9}.
\tag{11}
\]

Equation (7.8) immediately integrates the same bound from `Y^(1-epsilon/8)`. Because the lower endpoint in (4) lies strictly below that in (11), the stated application is not justified on the full interval.

This cannot be fixed merely by saying that the difference between `1/8` and `1/9` is a harmless constant: the issue is logical coverage of the interval on which the pointwise cap is used. A parameter choice must actually make the cap valid there.

## 2. The direct repair: keep `epsilon'=epsilon/8`

Corollary 6.3 already supplies the weighted lower bound on

\[
U:=Y^{1-\varepsilon/8}\le x\le Y.
\tag{12}
\]

There is no need for the upper cap to have coefficient exactly `epsilon` in its exponential. Set `epsilon'=epsilon/8` in (9)–(10). Then the comparison is valid on precisely the entire interval (12), and monotonicity of `omega` gives

\[
\frac{|M(x)|}{Z_0(x)}
\ll e^{q\varepsilon\omega_0},
\qquad
q=\frac98,
\qquad
\omega_0=\omega(Y).
\tag{13}
\]

Thus the extremal argument may use

\[
f(x)=Z_0(x)e^{q\varepsilon\omega_0},
\qquad
F(x)=|M(x)|,
\qquad
0\le F(x)\le f(x)
\tag{14}
\]

throughout `[U,Y]`.

The conditions of Corollary 6.3 remain unchanged. Take

\[
\kappa=\sqrt\varepsilon.
\tag{15}
\]

For sufficiently small `epsilon`, its required inequalities

\[
\sqrt\varepsilon\ge\kappa\ge\varepsilon,
\quad
\eta_0\le\varepsilon^2/100,
\quad
\gamma_0\le Y^{\varepsilon^2/100}
\]

hold exactly as in the printed Section 7 setup. Hence

\[
J(F):=
\int_U^Y
\frac{|M(x)|}{x^{1-\kappa}Z_0(x)}\,dx
\ge
J_0,
\tag{16}
\]

where

\[
J_0
=c^*\frac{\kappa Y^\kappa}
{\gamma_0^{C\kappa^{3/2}}(\log Y)^C}.
\tag{17}
\]

The only change from the printed proof is the harmless constant `q=9/8` multiplying `epsilon omega_0` in the cap.

## 3. The cutoff estimate works without dropping the lower endpoint

Pintz uses the elementary extremal principle that, for a positive decreasing weight `g` and a pointwise cap `0<=F<=f`, fixed lower weighted mass is achieved with minimal unweighted mass by saturating `f` from the left endpoint up to a cutoff `Y^*`.

Here

\[
g(x)=\frac{1}{x^{1-\kappa}Z_0(x)}
\]

is decreasing because

\[
g(x)=\gamma_0 x^{-2+\kappa+\eta_0}
\]

and `-2+kappa+eta_0<0` in the stated range.

Choose `Y^* in [U,Y]` so that

\[
\int_U^{Y^*} f(x)g(x)\,dx=J_0.
\tag{18}
\]

Such a cutoff exists because the actual `F=|M|` satisfies both `F<=f` and `J(F)>=J_0`, hence `J(f)>=J_0`.

Using (14), (18) is exactly

\[
\frac{e^{q\varepsilon\omega_0}}{\kappa}
\left((Y^*)^\kappa-U^\kappa\right)
=J_0.
\tag{19}
\]

The paper replaces the left side asymptotically by its `Y^*` term in (7.11). That replacement is not needed to obtain the crucial cutoff estimate. From (19) alone,

\[
(Y^*)^\kappa
\ge
\kappa e^{-q\varepsilon\omega_0}J_0,
\]

and therefore, using (17),

\[
\left(\frac{Y}{Y^*}\right)^\kappa
\ll
\frac{e^{q\varepsilon\omega_0}
\gamma_0^{C\kappa^{3/2}}(\log Y)^C}
{\kappa^2}.
\tag{20}
\]

This is the one-sided estimate actually needed downstream.

Taking logarithms and dividing by `kappa=sqrt(epsilon)` gives contributions of sizes

\[
O(\sqrt\varepsilon\,\omega_0),
\qquad
O(\varepsilon^{1/4}\log\gamma_0),
\qquad
O_\varepsilon(\log\log Y).
\tag{21}
\]

Pintz's (7.13) gives

\[
\omega_0\gg\sqrt{\log Y},
\qquad
\log\gamma_0\le\omega_0.
\tag{22}
\]

For sufficiently small fixed `epsilon`, `epsilon^(1/4)` is eventually dominated by `epsilon^(1/5)` up to the absolute constants in (21), while for that fixed `epsilon` the `log log Y` term is `o(omega_0)`. Thus (20) yields, after increasing the lower threshold in `Y`,

\[
\boxed{
\frac{Y}{Y^*}
\ll_\varepsilon e^{\varepsilon^{1/5}\omega_0}.}
\tag{23}
\]

The coefficient `q=9/8` changes only the smaller `sqrt(epsilon) omega_0` contribution and therefore does not affect the `epsilon^(1/5)` envelope.

## 4. The lower endpoint is negligible a posteriori

To turn the extremal cutoff into an unweighted lower bound, one must evaluate

\[
\int_U^{Y^*}f(x)\,dx
=
\frac{e^{q\varepsilon\omega_0}}{\gamma_0}
\frac{(Y^*)^{2-\eta_0}-U^{2-\eta_0}}{2-\eta_0}.
\tag{24}
\]

Here the lower endpoint really does need to be negligible relative to `Y^*`. Equation (23), together with

\[
U=Y^{1-\varepsilon/8},
\]

gives

\[
\frac{U}{Y^*}
\ll_\varepsilon
\exp\!\left(
-\frac{\varepsilon}{8}\log Y
+\varepsilon^{1/5}\omega_0
\right).
\tag{25}
\]

In the `vartheta=1` case under discussion, Pintz's (5.7) states

\[
\omega(Y)=o(\log Y).
\tag{26}
\]

For every fixed `epsilon>0`, (25) therefore tends to zero. Hence

\[
(Y^*)^{2-\eta_0}-U^{2-\eta_0}
\sim (Y^*)^{2-\eta_0},
\tag{27}
\]

which supplies the missing a-posteriori justification for the lower-end omission in the unweighted extremal integral.

Using (23) in (24), and discarding the favorable factor `e^{q epsilon omega_0}`, gives

\[
\int_U^Y |M(x)|\,dx
\gg_\varepsilon
\frac{Y^{2-\eta_0}}{\gamma_0}
 e^{-C\varepsilon^{1/5}\omega_0}
\tag{28}
\]

for an absolute constant `C`. Since `rho_0` attains `Z(Y)`,

\[
Z(Y)=\frac{Y^{1-\eta_0}}{\gamma_0},
\]

and division by `Y` yields (8).

As `epsilon` can be chosen arbitrarily small, a fixed absolute factor `C` in front of `epsilon^(1/5)` does not alter the logarithmic asymptotic conclusion.

## 5. Consequence for the Pintz audit chain

The current audit now isolates three independent presentation defects in the fresh preprint, each with an explicit repair:

1. `MC-010`: Corollary 6.3's terminal endpoint does not follow literally from Theorem 6.1 with the same parameter; constant rescaling `Y -> Ye^{-3}` repairs it.
2. `MC-011`: equation (6.23) drops a linear shifted-height factor; retaining that factor and restoring the theorem's existing `gamma_0` normalization repairs the theorem-level estimate.
3. `MC-012`: Section 7 chooses `epsilon'=epsilon/9` but then integrates the resulting cap down to the `epsilon/8` window; keeping `epsilon'=epsilon/8` and accepting the harmless `9/8` exponential constant repairs the global lower-bound assembly.

The third repair also avoids relying on the unproved `sim` simplification in printed equation (7.11): the exact cutoff identity already gives the required one-sided ratio estimate, and `omega(Y)=o(log Y)` then makes the lower endpoint negligible where it is actually needed.

These repairs substantially reduce the known local proof gaps behind the mean-absolute zero-boundary claim in `MC-009`. They do **not** yet justify removing `NEEDS-AUDIT`, because Section 7 still imports the Section 5 pointwise upper bound (5.9), whose contour construction depends on the earlier `1/zeta(s)` estimates and zero-avoiding contour machinery. Those load-bearing inputs have not been independently reconstructed end-to-end by this audit chain.

## Prior art and novelty assessment

`MC-S19` is the primary object under audit. The mismatch is visible directly between Pintz's displayed equations (7.7) and (7.8), and the repair uses only the same inequalities, Corollary 6.3, and the asymptotic `omega(Y)=o(log Y)` already present in the paper.

No novelty is claimed for Pintz's extremal principle, his theorem, or any new estimate for `M(x)`. A targeted search for the week-old preprint found only version `v1`/metadata mirrors and no erratum or correction addressing the Section 7 parameter mismatch. The durable Mathia contribution is therefore a proof audit and explicit repair of fresh prior art, not a new Möbius bound.

## Boundaries and falsification tests

This finding does not establish Pintz's Theorems 2.1–2.2 independently and does not upgrade `MC-009` beyond `NEEDS-AUDIT`.

The repair would fail if any of the following were false:

- the comparison (7.5)–(7.7) remains valid after choosing `epsilon'=epsilon/8`;
- Corollary 6.3 is available on the full interval `[Y^(1-epsilon/8),Y]` under `kappa=sqrt(epsilon)`;
- the extremal weight `g(x)=gamma_0 x^(-2+kappa+eta_0)` is decreasing;
- `omega(Y) >> sqrt(log Y)` and `log gamma_0<=omega(Y)` fail in the stated `vartheta=1` setup;
- `omega(Y)=o(log Y)` fails, preventing (25) from tending to zero.

The displayed hypotheses and equations (5.7), (6.25)–(6.27), and (7.13) supply these properties within the paper's stated framework. The remaining uncertainty is therefore upstream, especially the independent validity and uniformity of the Section 5 contour upper bound used in (7.7), rather than the Section 7 parameter bookkeeping repaired here.

## Consequences for the research line

For the Möbius Cancellation program, the mean-absolute endpoint remains a viable **literature-supplied target reduction** rather than established internal mathematics: if Pintz's theorem survives complete audit, proving an independently arithmetic RH-scale bound for `D_M` would already force the rightmost zero boundary to `1/2`.

The next theorem-audit target should move upstream rather than continue polishing Section 7 constants: reconstruct the Section 5 zero-avoiding contour and the bound (5.9), checking that its `epsilon`, zero-height, truncation, and uniformity dependencies support the substitutions used here. Until that succeeds, local/multiscale transfer work should continue to treat the mean-absolute endpoint as conditional on `MC-S19`, exactly as `MC-009` currently records.