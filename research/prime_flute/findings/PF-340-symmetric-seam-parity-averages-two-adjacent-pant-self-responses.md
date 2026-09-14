# PF-340 — symmetric seam parity averages two adjacent pant self-responses

**Status:** `EXACT-DERIVED + TWO-PANT-DECOMPOSITION + CANCELLATION-GATE + ROUTE-NARROWING`.

PF-339 reduces the live PF-336 translation route to an explicit two-mode test in the symmetric seam face-parity channel. The raw threshold itself is correct, but the simultaneous PF-214 cut adds one load-bearing bookkeeping point: the symmetric face-parity compression on cuff module `n` is **not the self-response of one one-cusp pant**. It is the average of the two self-responses contributed by the pant cores on the two sides of that cuff.

This matters for the proposed scalar PDE falsifier. Let `A_n^-` be the raw self-DtN block seen from the `Sigma_n^-` face through the left pant core `E_{n-1}`, with the other finite interface of that pant set to zero, and let `A_n^+` be the analogous self-DtN block seen from `Sigma_n^+` through the right pant core `E_n`. If

\[
S_{n,+}f:=2^{-1/2}(f,f)
\]

is the symmetric face-parity embedding, then PF-214's exact decomposition of the exterior energy gives

\[
\boxed{
\Lambda_n^{(+)}
=S_{n,+}^*\,Q_n\Lambda_EQ_n\,S_{n,+}
=\frac12\bigl(A_n^-+A_n^+\bigr)
}
\]

on every common retained physical-low cuff subspace. Thus every PF-339 fixed Fourier matrix element is exactly

\[
\boxed{
\lambda_{n;jk}^{(+)}
=\frac12\left(
\lambda_{n;jk}^-+\lambda_{n;jk}^+
\right),
}
\]

where the two terms come from **different adjacent pant cores**.

For PF-339's explicit half-cuff pair

\[
f_{n,+}=\frac{c_{n,2}+c_{n,1}}{\sqrt2},
\qquad
f_{n,-}=\frac{c_{n,2}-c_{n,1}}{\sqrt2},
\]

write

\[
\Delta_n^\pm
:=
\langle f_{n,+},A_n^\pm f_{n,+}\rangle
-
\langle f_{n,-},A_n^\pm f_{n,-}\rangle.
\]

Then the actual symmetric-module contrast is

\[
\boxed{
\Delta_n^{\mathrm{sym}}
:=
\langle f_{n,+},\Lambda_n^{(+)}f_{n,+}\rangle
-
\langle f_{n,-},\Lambda_n^{(+)}f_{n,-}\rangle
=rac12\bigl(\Delta_n^-+\Delta_n^+\bigr).
}
\]

Therefore the PF-339 necessary condition is equivalently

\[
\boxed{
\Delta_n^-+\Delta_n^+=o(w_n)
}
\]

along the PF-324 subsequence `r_n=h_{n+1}/h_n -> 0` if the PF-336 translation gate survives.

The consequence is a genuine extra cancellation gate. A lower bound such as

\[
|\Delta_n^+|\gtrsim w_n
\]

for the right pant `E_n` **does not by itself falsify** the symmetric-channel route: it is still logically possible that the left pant contributes an opposite contrast of the same size. To close PF-339 negatively one must estimate the two-pant sum, prove a common sign/no-cancellation principle for the two self-responses, or show that one side is asymptotically negligible relative to the other.

This distinction is particularly important on the arithmetic subsequence used by PF-338/PF-339. The condition

\[
r_n=\frac{h_{n+1}}{h_n}\to0
\]

controls the right pant distance

\[
s_n=\frac{h_n+h_{n+1}}2,
\]

but says nothing by itself about the left ratio `h_{n-1}/h_n` and hence nothing comparable about

\[
s_{n-1}=\frac{h_{n-1}+h_n}2.
\]

So the tempting strategy of proving a strong right-pant corridor contrast and silently treating it as the full symmetric-module contrast is not justified by the `r_n -> 0` arithmetic regime.

## Claim

Use the PF-214 simultaneous seam cut. Module `n` has boundary-energy space

\[
\mathcal B_n
=\mathcal H(\Sigma_n^-)
\oplus
\mathcal H(\Sigma_n^+).
\]

The left pant core `E_{n-1}` meets `\Sigma_{n-1}^+` and `\Sigma_n^-`, while the right pant core `E_n` meets `\Sigma_n^+` and `\Sigma_{n+1}^-`. Let

\[
A_n^-:=(\Lambda_{E_{n-1}})_{\Sigma_n^-,\Sigma_n^-},
\qquad
A_n^+:=(\Lambda_{E_n})_{\Sigma_n^+,\Sigma_n^+}
\tag{1}
\]

be their self-DtN blocks after setting the other finite interface datum of the corresponding pant to zero.

Then:

1. the diagonal raw exterior block on module `n` is exactly
   \[
   \boxed{
   Q_n\Lambda_EQ_n
   =A_n^-\oplus A_n^+;
   }
   \tag{2}
   \]
2. for the symmetric face-parity isometry
   \[
   S_{n,+}:f\mapsto2^{-1/2}(f,f),
   \tag{3}
   \]
   the same-channel raw compression is
   \[
   \boxed{
   S_{n,+}^*Q_n\Lambda_EQ_nS_{n,+}
   =\frac12(A_n^-+A_n^+);
   }
   \tag{4}
   \]
3. equation (4) remains true after compression to any common physical Fourier band, in particular PF-318's retained nonconstant low band;
4. for every pair of retained Fourier modes,
   \[
   \boxed{
   \lambda_{n;jk}^{(+)}
   =\frac12\bigl(
   \langle e_{n,j},A_n^-e_{n,k}\rangle
   +
   \langle e_{n,j},A_n^+e_{n,k}\rangle
   \bigr);
   }
   \tag{5}
   \]
5. for the PF-339 vectors `f_{n,+},f_{n,-}`, the symmetric energy contrast is the average of the two adjacent pant contrasts,
   \[
   \boxed{
   \Delta_n^{\mathrm{sym}}
   =\frac12(\Delta_n^-+\Delta_n^+).
   }
   \tag{6}
   \]

Hence PF-339's implication

\[
\Delta_n^{\mathrm{sym}}=o(w_n)
\tag{7}
\]

is a statement about the **two-pant sum**. A one-pant estimate can refute (7) only after an additional no-cancellation estimate controls the other summand.

## 1. PF-214 makes the diagonal module block a direct sum

PF-214 gives the exact exterior form identity

\[
\lambda_E(\varphi)
=\sum_m
\lambda_{E_m}
\bigl(\varphi_m^+,\varphi_{m+1}^-\bigr).
\tag{8}
\]

Take boundary data supported only on module `n`,

\[
\varphi_m=0\quad(m\ne n),
\qquad
\varphi_n=(u,v).
\]

Only `E_{n-1}` and `E_n` survive in (8), and their other finite-interface data are zero. Therefore

\[
\lambda_E(\varphi)
=
\lambda_{E_{n-1}}(0,u)
+
\lambda_{E_n}(v,0)
=
\langle u,A_n^-u\rangle
+
\langle v,A_n^+v\rangle.
\tag{9}
\]

There is no `u-v` cross term: the two variables belong to different disconnected pant cores after the simultaneous cut. Equation (9) is exactly the quadratic-form statement (2).

Now put `u=v=f/\sqrt2`. Equation (9) becomes

\[
\langle S_{n,+}f,\Lambda_ES_{n,+}f\rangle
=
\frac12\langle f,A_n^-f\rangle
+
\frac12\langle f,A_n^+f\rangle,
\]

which proves (4). Polarization gives (5), and applying the same identity separately to `f_{n,+}` and `f_{n,-}` proves (6).

Nothing in this argument depends on the seam-width asymptotics or on the arithmetic subsequence. It is an exact consequence of the simultaneous-cut topology before seam normalization.

## 2. Zero twist aligns the test, but does not prove the sign

PF-217 already uses the zero-twist seam marking to center the same tangential boundary profile at the finite-finite common-perpendicular foot on **both** artificial boundary circles of a module. Thus the two adjacent self-responses in (6) can be tested with the same physical half-cuff translation and the same explicit `f_{n,+},f_{n,-}` pair. There is no hidden phase-welding problem between the two faces.

That coherence does not imply

\[
\operatorname{sgn}\Delta_n^-
=
\operatorname{sgn}\Delta_n^+.
\]

The adjacent pants have different other cuff lengths and therefore different global completions. PF-215 gives a strong local conductance mechanism near each finite-finite common perpendicular, but PF-339 already notes that such a local corridor estimate is not a total-energy comparison. The direct-sum identity above makes clear that the same missing global control is required on **both sides together**, or else in a theorem that prevents their contrasts from canceling.

## 3. The `r_n -> 0` regime controls only one neighboring pant

PF-215 gives the exact finite-finite cuff distance

\[
s_m=\frac{h_m+h_{m+1}}2.
\tag{10}
\]

The PF-324/PF-338 subsequence assumes

\[
\frac{h_{n+1}}{h_n}\to0,
\]

so

\[
s_n=\frac{h_n}{2}(1+o(1)).
\tag{11}
\]

This is useful for the right pant `E_n`. But the left pant in the same symmetric module has

\[
s_{n-1}=\frac{h_{n-1}+h_n}{2},
\tag{12}
\]

and (11) gives no estimate for `h_{n-1}/h_n`. In particular no argument may discard `\Delta_n^-`, assign it the right-pant scale, or assume it has the same asymptotic sign merely from `r_n -> 0`.

This is the exact point at which a one-sided corridor calculation stops being a complete PF-339 falsifier.

## 4. What would now close the two-mode test

Equation (6) leaves three clean ways to finish the obstruction:

- **common sign:** prove `\Delta_n^-\Delta_n^+\ge0` eventually and obtain `|\Delta_n^-|+|\Delta_n^+|\not=o(w_n)`;
- **dominance:** prove one contrast is `\not=o(w_n)` while the other is asymptotically smaller than it;
- **direct sum estimate:** estimate `\Delta_n^-+\Delta_n^+` without separating the two pants.

These are alternatives, not additional requirements to stack. The first would be particularly useful because PF-217 already fixes a common zero-twist origin for the two boundary profiles. But no common-sign theorem is presently established.

A right-pant estimate alone remains valuable input: on `r_n -> 0` it is the side whose short corridor has the cleanest arithmetic scale. It simply has to be combined with one of the no-cancellation mechanisms above before it can be promoted to a contradiction of PF-336.

## Prior-art and novelty audit

The facts that Dirichlet-to-Neumann/Steklov--Poincare operators decompose over disconnected subdomains and that interface operators can be organized blockwise are standard domain-decomposition machinery. A targeted literature check found only this general framework; no novelty is claimed for (2)--(4) as abstract operator algebra.

The Mathia-specific content is the interaction of PF-214's exact one-cusp-pant chain decomposition with PF-339's **symmetric seam face-parity** test. That combination exposes a cancellation channel hidden by the phrase "one-cusp-pant energy": the quantity amplified by the symmetric seam normalizer is the average of the two adjacent pant self-responses. No external theorem is imported into the derivation, so `SOURCES.md` needs no new dependency.

## Boundaries and falsification

1. **PF-339's raw threshold is unchanged.** The conclusion `\lambda_{n;jk}^{(+)}=o(w_n)` under the PF-336 translation gate remains valid. This finding only identifies exactly what raw operator is being tested.
2. **No cancellation is asserted to occur.** Equation (6) says it is logically available until a sign, dominance, or direct-sum estimate rules it out.
3. **No sign theorem is inferred from zero twist.** Zero twist aligns the seam coordinates and common test profile; it does not make the two adjacent pant DtN self-blocks equal.
4. **No arithmetic statement about the left ratio is added.** `r_n -> 0` controls `h_{n+1}/h_n`; it does not control `h_{n-1}/h_n`.
5. **The identity is local to the diagonal cuff-module block.** Neighboring off-diagonal module blocks of `\Lambda_E` remain the genuine two-boundary cross responses of a single pant and are not represented by (4).
6. **No completed-angle, scattering, determinant, zeta-zero, critical-line, or RH conclusion follows.**

A falsification would require a failure of PF-214's exact exterior decomposition (8), a mismatch between the symmetric face-parity embedding and the channel used in PF-339, or an omitted face cross term inside the diagonal module block. The simultaneous-cut topology rules out that last possibility because `\Sigma_n^-` and `\Sigma_n^+` belong to distinct connected components of `E`.

## Consequence for the research line

The next two-mode PDE calculation should not stop after showing that the right pant `E_n` distinguishes `f_{n,+}` from `f_{n,-}`. The actual scalar target inherited from PF-339 is

\[
\boxed{
\frac{|\Delta_n^-+\Delta_n^+|}{w_n}
\not\longrightarrow0.
}
\]

The `r_n -> 0` geometry makes `E_n` the natural first side to estimate, but a publication-grade obstruction must additionally control the left self-response well enough to exclude cancellation. This is now the cheapest exact remaining gate before returning to higher odd modes or a positive full-commutator estimate.