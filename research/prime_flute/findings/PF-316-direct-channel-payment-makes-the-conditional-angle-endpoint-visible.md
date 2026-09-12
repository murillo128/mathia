# PF-316 — direct-channel payment makes the conditional angle visible at the weak-trace endpoint

**Status:** `EXACT-DERIVED + CLASSICAL-SINGULAR-VALUE-CALCULUS + PHYSICAL-ANGLE-ENDPOINT-EQUIVALENCE + POSITIVE/ROUTE-SHARPENING`.

[[research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect|PF-315]] writes the full PF-281 physical `P/H` angle, after a unitary change of physical-low coordinates, as

\[
U_PT_{P/H}
=
\binom{T_HV_H}{Z_{LH}},
\qquad
V_H^*V_H=I-Z_{LH}^*Z_{LH}.
\tag{1}
\]

PF-315 therefore leaves two source-reached channels: the direct retained-low/high angle `Z_{LH}` and the conditional post-low angle `T_H` fed through the canonical residual map `V_H`. It proves that a **uniform** gap of `Z_{LH}` from one makes `V_H` uniformly invertible, but without such a gap it still appeared possible that `V_H` might hide bad singular-value behavior of `T_H` while the direct channel remained tolerable.

At the compactness and weak-trace scales relevant to the current endpoint, that possibility disappears. The attenuation in `V_H` is paid for quantitatively by the singular values of `Z_{LH}` itself.

On every finite canonical section let

\[
V_H=W_HD_H,
\qquad
D_H:=|V_H|=(I-Z_{LH}^*Z_{LH})^{1/2}
\tag{2}
\]

be the polar decomposition. Strict positivity of the finite section makes `V_H` invertible, hence `W_H` is unitary. Put

\[
C_H:=I-D_H.
\tag{3}
\]

Then

\[
0\le C_H
=I-(I-Z_{LH}^*Z_{LH})^{1/2}
\le Z_{LH}^*Z_{LH},
\tag{4}
\]

and, more sharply,

\[
\boxed{
 s_j(C_H)
 =1-\sqrt{1-s_j(Z_{LH})^2}
 \le s_j(Z_{LH})^2.
}
\tag{5}
\]

Since

\[
T_HW_H
=T_HV_H+T_HW_HC_H,
\tag{6}
\]

Fan's singular-value inequality gives, for every `j>=1`,

\[
\boxed{
 s_{2j-1}(T_H)
 \le
 s_j(T_HV_H)+s_j(Z_{LH})^2.
}
\tag{7}
\]

Both terms on the right are compressions of the full angle in (1), so

\[
\boxed{
 s_{2j-1}(T_H)
 \le
 s_j(T_{P/H})+s_j(T_{P/H})^2.
}
\tag{8}
\]

This is the missing converse visibility estimate. A conditional direction cannot be strongly suppressed by the residual source without producing an equally visible direct-channel payment. In particular, **the full physical angle can be compact or weak trace class only if `T_H` itself is compact or weak trace class**, even when `Z_{LH}` has no uniform gap from one.

Conversely, if `T_H` and `Z_{LH}` are weak trace class, then so are `T_HV_H` and the block column (1). Hence, for the canonical finite-section endpoint budgets and for every compatible limiting realization,

\[
\boxed{
T_{P/H}\in\mathcal S_{1,\infty}
\iff
T_H\in\mathcal S_{1,\infty}
\ \text{and}\ 
Z_{LH}\in\mathcal S_{1,\infty}.
}
\tag{9}
\]

The same argument gives the compactness equivalence

\[
\boxed{
T_{P/H}\text{ compact}
\iff
T_H\text{ compact and }Z_{LH}\text{ compact}.
}
\tag{10}
\]

Thus PF-315's residual map `V_H` is still essential for exact representation, but it is **not a third endpoint regularizer**. For weak-trace work the physical problem reduces to two genuine angle estimates, `T_H` and `Z_{LH}`. If `T_H` violates the endpoint, the full physical angle violates it regardless of how strongly `V_H` attenuates the offending directions; the attenuation can occur only by making `Z_{LH}` large enough to pay for it.

## Claim

Work on any finite canonical PF-205/PF-311 section with the notation of PF-315. Set

\[
F:=T_{P/H},
\qquad
T:=T_H,
\qquad
Z:=Z_{LH},
\qquad
V:=V_H.
\tag{11}
\]

Then, after the PF-315 unitary on the physical-low side,

\[
F\simeq
\binom{TV}{Z},
\qquad
V^*V=I-Z^*Z,
\qquad
\|F\|,\|T\|,\|Z\|,\|V\|<1.
\tag{12}
\]

For every singular index `j>=1`:

1. if `V=W D` is the polar decomposition, then `W` is unitary and
   \[
   D=(I-Z^*Z)^{1/2};
   \tag{13}
   \]
2. for `C:=I-D`,
   \[
   \boxed{
   0\le C\le Z^*Z,
   \qquad
   s_j(C)
   =1-\sqrt{1-s_j(Z)^2}
   \le s_j(Z)^2;
   }
   \tag{14}
   \]
3. the conditional angle obeys the singular-value recovery estimate
   \[
   \boxed{
   s_{2j-1}(T)
   \le s_j(TV)+s_j(Z)^2;
   }
   \tag{15}
   \]
4. using PF-315 compression monotonicity,
   \[
   \boxed{
   s_{2j-1}(T)
   \le s_j(F)+s_j(F)^2;
   }
   \tag{16}
   \]
5. the counting functions therefore satisfy, for every `0<a<1`,
   \[
   \boxed{
   N_T(a+a^2)
   \le 2N_F(a);
   }
   \tag{17}
   \]
6. in the weak-trace quasi-norm convention
   \[
   \|A\|_{1,\infty}^{\#}:=\sup_{j\ge1}j\,s_j(A),
   \tag{18}
   \]
   every finite section satisfies
   \[
   \boxed{
   \|T\|_{1,\infty}^{\#}
   \le
   2\|F\|_{1,\infty}^{\#}
   +2\bigl(\|F\|_{1,\infty}^{\#}\bigr)^2;
   }
   \tag{19}
   \]
   while `Z` is a row compression of `F`, so
   \[
   \boxed{
   \|Z\|_{1,\infty}^{\#}
   \le \|F\|_{1,\infty}^{\#};
   }
   \tag{20}
   \]
7. conversely,
   \[
   \boxed{
   s_{2j-1}(F)
   \le s_j(T)+s_j(Z),
   }
   \tag{21}
   \]
   and hence
   \[
   \boxed{
   \|F\|_{1,\infty}^{\#}
   \le
   2\bigl(
   \|T\|_{1,\infty}^{\#}
   +\|Z\|_{1,\infty}^{\#}
   \bigr).
   }
   \tag{22}
   \]

Consequently a nested family of canonical finite sections has a uniform weak-`S_1` bound for the full physical angle if and only if it has uniform weak-`S_1` bounds for both the conditional post-low angle and the direct retained-low/high angle. The constants above are deliberately crude; the structural equivalence, not constant optimization, is the point.

The same singular-value inequalities imply the analogous equivalence for compactness and for strong Schatten `S_p`, `p>0`, whenever the corresponding limiting operators are defined through the canonical exhaustion.

## 1. The residual map is identity minus a quadratic direct-channel defect

PF-315 gives

\[
V^*V=I-Z^*Z.
\tag{23}
\]

On a finite strictly positive section `V` is invertible, because both `R_H` and `J_{HH}` in

\[
V=R_H^{1/2}J_{HH}^{-1/2}
\]

are strictly positive. Its polar factor is therefore a unitary `W`, and

\[
D=|V|=(V^*V)^{1/2}=(I-Z^*Z)^{1/2}.
\tag{24}
\]

The scalar function

\[
f(t)=1-\sqrt{1-t},
\qquad 0\le t<1,
\]

is increasing and satisfies

\[
0\le f(t)\le t.
\tag{25}
\]

Functional calculus therefore gives

\[
C=I-D=f(Z^*Z),
\qquad 0\le C\le Z^*Z.
\tag{26}
\]

Because `f` is increasing, the eigenvalues of `C` are obtained by applying `f` to the eigenvalues of `Z^*Z`. Hence

\[
s_j(C)
=f(s_j(Z)^2)
=1-\sqrt{1-s_j(Z)^2}
\le s_j(Z)^2,
\tag{27}
\]

which proves (14).

This quadratic payment is the key point. A singular direction on which `V` differs appreciably from its unitary polar factor must already carry direct `L/H` correlation through `Z`; small singular values of `Z` make the deviation of `V` from a unitary **quadratically** smaller.

For later ideal bookkeeping there is also the exact rationalized identity

\[
C
=Z^*Z\bigl(I+(I-Z^*Z)^{1/2}\bigr)^{-1}.
\tag{28}
\]

Thus, whenever `Z` is Hilbert--Schmidt, `C` is trace class. In particular,

\[
Z\in\mathcal S_{1,\infty}
\Longrightarrow
Z\in\mathcal S_2
\Longrightarrow
C\in\mathcal S_1.
\tag{29}
\]

This is another way to read the endpoint equivalence: after the direct channel has paid the weak-trace budget, the residual map is a trace-class perturbation of a unitary on each finite section.

## 2. Fan's inequality recovers the hidden conditional singular values

From `V=WD`,

\[
TV=TWD.
\tag{30}
\]

Therefore

\[
TW-TV
=TW(I-D)
=TWC.
\tag{31}
\]

Since `W` is unitary,

\[
s_j(TW)=s_j(T).
\tag{32}
\]

Since `T` is a contraction and `W` is unitary,

\[
s_j(TWC)\le s_j(C)\le s_j(Z)^2.
\tag{33}
\]

Apply the classical Fan inequality

\[
s_{j+k-1}(A+B)\le s_j(A)+s_k(B)
\tag{34}
\]

to

\[
TW=TV+TWC
\]

with `j=k`. Equations (32)--(33) give

\[
s_{2j-1}(T)
\le s_j(TV)+s_j(Z)^2,
\]

which is (15).

PF-315 already proves that `TV` and `Z` are orthogonal-row compressions of `F`. Hence

\[
s_j(TV)\le s_j(F),
\qquad
s_j(Z)\le s_j(F),
\tag{35}
\]

and (16) follows.

Equation (16) is stronger than the previous uniform-gap statement for endpoint purposes. PF-315 equation (18) needed a fixed `delta>0` to compare `T` and `TV` singular value by singular value at the **same index**. The present result allows `V` to become arbitrarily small, but pays for that loss with `Z` and only spends one fixed factor of two in the singular index. That is exactly enough for compactness, Schatten ideals, and weak-`S_1` counting.

## 3. Counting consequence: a bad conditional angle is a genuine full-angle obstruction

Let

\[
N_A(a):=\#\{j:s_j(A)>a\}.
\]

Put `r=N_F(a)`. Then

\[
s_{r+1}(F)\le a.
\]

Equation (16) with `j=r+1` gives

\[
s_{2r+1}(T)
\le a+a^2.
\]

Thus at most `2r` singular values of `T` can exceed `a+a^2`, which proves (17):

\[
N_T(a+a^2)\le2N_F(a).
\]

This is the operational version of the theorem. Any geometric construction that produces too many singular directions of the conditional post-low angle `T_H` is already a **necessary endpoint obstruction** for the full physical `P/H` angle. One does not have to prove a uniform gap for `Z_{LH}` or separately show that those directions survive `V_H`.

If `V_H` suppresses them, equation (23) forces the direct channel to pay. The full angle sees either the conditional component or the direct component, and (17) quantifies that alternative at the level of singular-value counts.

In particular, if for some sequence `a_m\downarrow0`

\[
a_m N_{T_H}(2a_m)\longrightarrow\infty,
\tag{36}
\]

then the full angle cannot lie in weak trace class. For small `a`, `a+a^2<2a`, so (17) gives

\[
N_{T_H}(2a)
\le N_{T_H}(a+a^2)
\le2N_{T_{P/H}}(a).
\tag{37}
\]

A divergence on the left therefore forces the corresponding weak-trace counting budget to fail for the full physical angle.

This is materially different from PF-284's earlier heavy-angle sufficient/necessary sandwich. Here `T_H` is not an arbitrary auxiliary angle: PF-315 proves it is the exact conditional angle generated by sequential physical-band elimination, and the direct-channel defect identity forces any source attenuation to reappear inside the same full physical angle.

## 4. Weak trace is exactly the pair `T_H` plus `Z_{LH}`

Assume first that the full finite-section family has

\[
M:=\sup j\,s_j(F)<\infty.
\tag{38}
\]

Equation (16) gives

\[
s_{2j-1}(T)
\le \frac{M}{j}+\frac{M^2}{j^2}.
\tag{39}
\]

Monotonicity of singular values handles the even indices, yielding the crude uniform bound

\[
\sup_k k\,s_k(T)
\le2M+2M^2.
\tag{40}
\]

The direct channel is a compression, so

\[
\sup_j j\,s_j(Z)\le M.
\tag{41}
\]

Thus full weak trace forces weak trace of **both** downstream channels.

Conversely, `V` is a contraction, so

\[
s_j(TV)\le s_j(T).
\tag{42}
\]

Write the block column as the sum of two orthogonally embedded operators,

\[
\binom{TV}{Z}
=
\binom{TV}{0}
+
\binom{0}{Z}.
\tag{43}
\]

Another application of Fan's inequality gives

\[
s_{2j-1}(F)
\le s_j(TV)+s_j(Z)
\le s_j(T)+s_j(Z),
\tag{44}
\]

which yields (21)--(22). Therefore the full endpoint is equivalent to the pair of endpoint estimates.

The same proof gives more than the weak endpoint. If `F` is compact, (16) forces `T` compact and compression forces `Z` compact. Conversely compact `T,Z` make both rows in (43) compact. Likewise, for every strong Schatten exponent `p>0`, (16) and (44) give equivalence of `S_p` membership up to the harmless index dilation.

No claim is made here about a new abstract operator ideal. These are elementary consequences of polar decomposition, functional calculus, compression monotonicity, and Fan inequalities. Their significance is that the PF-315 physical decomposition satisfies exactly the defect identity needed to apply them.

## 5. Consequence for the current Prime Flute frontier

The frontier after PF-315 was phrased as a two-component source-reached problem: determine whether `Z_{LH}` has a heavy/noncompact range and, if it is uniformly gapped, transfer the remaining singular-value problem to `T_H`; otherwise estimate `Z_{LH}` and `T_HV_H` together.

The present result sharpens that division.

For **endpoint falsification**, `T_H` may now be studied directly. If `T_H` fails compactness or weak trace class, the full physical angle fails as well; `V_H` cannot save it. No direct-channel gap hypothesis is needed.

For **endpoint proof**, one must prove both

\[
Z_{LH}\in\mathcal S_{1,\infty}
\qquad\text{and}\qquad
T_H\in\mathcal S_{1,\infty}.
\tag{45}
\]

These two statements are sufficient by (44), and each is necessary by (16) and compression. The residual factor `V_H` need not receive an independent ideal estimate.

This changes the cheapest next tests. The direct channel `Z_{LH}` is still a real physical gate, but it should no longer be used only to decide whether `V_H` is invertible. Its own weak-trace estimate is one half of the final endpoint. Independently, any local or global geometry that yields a conditional `T_H` counting obstruction is already decisive for the full route.

In particular, PF-310--PF-311's screened constant/high geometry remains relevant without first resolving whether the direct low/high channel is uniformly separated from one. Conversely, PF-212's local physical frequency estimates and the older reassembly machinery can be asked directly whether they control `Z_{LH}` in weak trace class. The two estimates then meet through (9), rather than through a separate source-overlap theory for `V_H`.

This does **not** close either geometric estimate. It removes a representation ambiguity: source attenuation between the full angle and the conditional angle cannot improve compactness or the weak-trace endpoint without the direct channel itself consuming the same singular directions.

## Prior art and novelty assessment

The abstract ingredients are standard operator-ideal calculus. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, AMS (2005), DOI `10.1090/surv/120`, is a standard source for singular values, symmetrically normed ideals, and Fan-type inequalities. The contraction-defect relation underlying PF-315/PF-312 is part of the classical Julia/Halmos contraction framework; P. L. Robinson, *Julia operators and Halmos dilations*, arXiv:1803.09329, records the familiar defect-operator intertwining identity. No novelty is claimed for polar decomposition, the inequality `1-sqrt(1-t)<=t`, Fan inequalities, weak-Schatten ideals, or the fact that trace-class perturbations do not leave a two-sided ideal.

A structure-directed literature audit found the expected general trace-ideal and contraction-defect theory, not a prime-flute-specific theorem. The durable Mathia-specific deduction is the combination with PF-315's exact physical-band Schur factorization. That factorization forces the same `Z_{LH}` which suppresses the residual source to appear as the orthogonal direct row of the **full target angle**, and this makes the conditional `T_H` endpoint visible without a uniform direct-channel gap.

## Boundary conditions and falsification tests

1. **Finite canonical sections are exact.** Equations (14)--(22) use the fact that the finite PF-205/PF-311 section is strictly positive, so `V_H` is invertible and its polar factor is unitary. This is already the setting in which the current endpoint budgets are tested.
2. **Infinite realization is inherited through the canonical exhaustion.** The weak-`S_1`, compactness, and `S_p` conclusions for a limiting operator require the same compatible Galerkin/exhaustion convergence used by PF-281/PF-315. The finite-section inequalities are uniform and therefore survive any realization for which singular-value ideal membership is obtained as the limit of those canonical sections.
3. **No estimate for either geometry is proved.** The theorem does not establish `Z_{LH}\in\mathcal S_{1,\infty}` or `T_H\in\mathcal S_{1,\infty}` for the prime flute. It only proves that these are exactly the two endpoint gates after PF-315.
4. **The squared payment is load-bearing.** Replacing (23) by a generic contraction source would destroy (14)--(16). The result is specific to the canonical residual map satisfying `V_H^*V_H=I-Z_{LH}^*Z_{LH}`.
5. **No uniform gap is assumed.** Singular values of `Z_{LH}` may approach one on finite sections. The price is then visible directly in `F`; the theorem does not infer bounded invertibility of `V_H`.
6. **No RH or spectral conclusion follows yet.** The result is an endpoint reduction for the PF-281 mixed physical angle. The global weak-trace reassembly, signed target composition, relative operator construction, determinant/scattering interpretation, prime/clone discrimination, critical-line statement, and RH consequence all remain separate gates.

A direct algebraic audit is to generate arbitrary finite contractions `Z,T`, set `D=(I-Z^*Z)^{1/2}`, choose any unitary `W`, put `V=WD`, and verify (15)--(22) numerically and symbolically. Failure of (15) in such a model would falsify the derivation. For the actual prime-flute route, the decisive next mathematical tests are independent estimates of the two genuine endpoint channels in (45).