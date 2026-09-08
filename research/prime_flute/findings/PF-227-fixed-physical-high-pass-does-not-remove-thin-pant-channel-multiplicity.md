# PF-227 — fixed physical high-pass does not remove thin-pant channel multiplicity

**Status:** `EXACT-DERIVED + GEOMETRIC-COUNTING + NEGATIVE/ROUTE-NARROWING`. PF-226 proves that the raw normalized pant crossing

\[
B_n=\Pi_{n+1}K\Pi_n
\]

has at least order `s_n^{-1}` singular channels above one fixed threshold, where

\[
s_n=\frac{h_n+h_{n+1}}2
\asymp \frac{g_n+g_{n+1}}{P_n}.
\]

PF-212 independently splits every seam module at a fixed **physical tangential frequency** and controls the resulting high-frequency Poisson factors. The two facts interact in a useful but initially ambiguous way: one might hope that PF-226's growing channel multiplicity sits mainly in the low sector and therefore disappears after the PF-212 low/high split. It does not.

Let `P_{\kappa,n}` be the PF-212 projection on the `n`th normalized seam-boundary module onto tangential Fourier frequencies `|2\pi k/L_n|\le\kappa`, and put

\[
H_{\kappa,n}=I-P_{\kappa,n}.
\]

For every fixed `\kappa\ge1` there are constants `\tau,c>0`, independent of `n`, such that after a finite head

\[
\boxed{
N_{H_{\kappa,n+1}B_nH_{\kappa,n}}(\tau)
\ge \frac{c}{s_n}
\asymp c\frac{P_n}{g_n+g_{n+1}}.
}
\]

More generally, the same conclusion holds for a varying physical cutoff `\kappa_n` whenever

\[
\boxed{
\kappa_n(L_n+L_{n+1})=o(s_n^{-1}).
}
\]

Thus removing any fixed, or even sufficiently slowly growing, physical-frequency sector costs only negligible dimension compared with the inverse-seam band constructed in PF-226. Using the unconditional Baker--Harman--Pintz gap envelope and `L_n=O(\log P_n)`, every cutoff satisfying

\[
\kappa_n=o\!\left(\frac{P_n^{0.475}}{\log P_n}\right)
\]

is certainly too small to remove the raw saturated multiplicity by dimensional truncation alone.

This does **not** contradict PF-212. PF-212 does not claim that high-pass projection makes the raw exterior crossing small; it proves singular-value decay for the **energy-normalized high-frequency Poisson factors** that occur in the actual recoupling words. PF-227 therefore sharpens the weak-trace frontier in a precise direction: the PF-212 split can still rescue the endpoint only through quantitative high-frequency damping after Poisson/resolvent dressing, not because the dangerous raw channels were confined to a low-dimensional low-frequency sector.

## Claim

Retain the simultaneous PF-205 seam decomposition and the notation of PF-212/PF-226. On the normalized boundary-energy space

\[
\mathcal B=\bigoplus_j\mathcal B_j,
\qquad
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\]

write

\[
B_n=\Pi_{n+1}K\Pi_n.
\tag{1}
\]

For a physical cutoff `\kappa\ge1`, let `P_{\kappa,n}` be the orthogonal projection on `\mathcal B_n` induced by the PF-212 two-boundary tangential Fourier cutoff

\[
\left|\frac{2\pi k}{L_n}\right|\le\kappa,
\tag{2}
\]

and let

\[
H_{\kappa,n}=I-P_{\kappa,n}.
\tag{3}
\]

PF-212 gives the uniform rank bound

\[
\boxed{
\operatorname{rank}P_{\kappa,n}
\le C(1+\kappa L_n).
}
\tag{4}
\]

Let `S_n\subset H_0^1(I)` and the injective normalized boundary maps

\[
\phi\mapsto f_n(\phi),
\qquad
\phi\mapsto f_{n+1}(\phi)
\]

be the fixed-window inverse-seam band from PF-226, with

\[
\dim S_n=m_n=\left\lfloor\frac{\eta}{s_n}\right\rfloor.
\tag{5}
\]

Here, to simplify notation, `f_{n+1}(\phi)` includes PF-226's uniformly controlled boundary identification `J_n\phi`. Define the doubly high witness space

\[
S_n^{\mathrm{hh}}=
\left\{
\phi\in S_n:
P_{\kappa_n,n}f_n(\phi)=0,
\quad
P_{\kappa_n,n+1}f_{n+1}(\phi)=0
\right\}.
\tag{6}
\]

Then pure finite-dimensional codimension counting gives

\[
\boxed{
\dim S_n^{\mathrm{hh}}
\ge
m_n-C\kappa_n(L_n+L_{n+1})-C.
}
\tag{7}
\]

Consequently, whenever

\[
\kappa_n(L_n+L_{n+1})=o(s_n^{-1}),
\tag{8}
\]

one has after a finite head

\[
\dim S_n^{\mathrm{hh}}\ge c s_n^{-1}.
\tag{9}
\]

For every nonzero `\phi\in S_n^{\mathrm{hh}}`, PF-226's exact cross-DtN identity and fixed-window estimates remain unchanged:

\[
\left|
\langle f_{n+1}(\phi),B_nf_n(\phi)\rangle
\right|
\ge
\frac{c}{s_n}\|\phi\|_2^2,
\tag{10}
\]

while

\[
\|f_n(\phi)\|^2
\le
Cw_n\left(1+\frac{\eta^2}{s_n^2}\right)\|\phi\|_2^2,
\tag{11}
\]

\[
\|f_{n+1}(\phi)\|^2
\le
Cw_{n+1}\left(1+\frac{\eta^2}{s_n^2}\right)\|\phi\|_2^2.
\tag{12}
\]

Because both witness vectors are high by construction,

\[
\langle f_{n+1}(\phi),B_nf_n(\phi)\rangle
=
\left\langle
f_{n+1}(\phi),
H_{\kappa_n,n+1}B_nH_{\kappa_n,n}f_n(\phi)
\right\rangle.
\tag{13}
\]

Exactly as in PF-226, the derivative term dominates the harmless `1` in (11)--(12) on the tail. Since

\[
w_n\asymp P_n^{-1},
\qquad
s_n\ge cP_n^{-1},
\tag{14}
\]

Cauchy--Schwarz in (13) yields a fixed `\tau>0` such that

\[
\boxed{
\|H_{\kappa_n,n+1}B_nH_{\kappa_n,n}f_n(\phi)\|
\ge
\tau\|f_n(\phi)\|
\qquad
(\phi\in S_n^{\mathrm{hh}}).
}
\tag{15}
\]

The map `\phi\mapsto f_n(\phi)` is injective, so the singular-value min--max principle gives

\[
\boxed{
N_{H_{\kappa_n,n+1}B_nH_{\kappa_n,n}}(\tau/2)
\ge
m_n-C\kappa_n(L_n+L_{n+1})-C.
}
\tag{16}
\]

Under (8), this becomes

\[
\boxed{
N_{H_{\kappa_n,n+1}B_nH_{\kappa_n,n}}(\tau/2)
\ge \frac{c}{s_n}.
}
\tag{17}
\]

For the canonical prime parameters, PF-205/PF-215/PF-226 give

\[
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\qquad
L_n+L_{n+1}=O(\log P_n).
\tag{18}
\]

The Baker--Harman--Pintz envelope `g_j=O(P_j^{0.525})`, together with `P_{n+1}/P_n\to1`, gives

\[
s_n\le CP_n^{-0.475},
\qquad
s_n^{-1}\ge cP_n^{0.475}.
\tag{19}
\]

Hence (8) certainly holds whenever

\[
\boxed{
\kappa_n=o\!\left(\frac{P_n^{0.475}}{\log P_n}\right).
}
\tag{20}
\]

Every fixed physical cutoff and every fixed polylogarithmic physical cutoff therefore leave order `s_n^{-1}` raw high--high singular channels above a fixed threshold.

## 1. Why the codimension argument is enough

No approximate preservation of Fourier modes through the pant is required. The source condition

\[
P_{\kappa_n,n}f_n(\phi)=0
\]

and the target condition

\[
P_{\kappa_n,n+1}f_{n+1}(\phi)=0
\]

are imposed independently. Each is a linear constraint of codimension at most the rank of the corresponding low-frequency projection. Therefore their simultaneous kernel inside the `m_n`-dimensional PF-226 witness band loses at most the sum of those two ranks, proving (7).

This point matters because PF-226's normal-ray boundary identification `J_n` need not preserve global cuff Fourier modes. The argument does not assume that it does. The target high-frequency condition is enforced after applying the actual `J_n`.

## 2. The PF-226 coercive band survives the high--high compression

The key lower estimate in PF-226 is variational and holds for **every** `\phi\in S_n`, not merely for a preferred basis. Restricting to the subspace `S_n^{\mathrm{hh}}` therefore preserves the opposite-versus-same-sign energy gap and the cross-form lower bound (10).

Likewise, PF-226's strip-normalization bounds are uniform over all of `S_n`. Nothing in the proof of (11)--(12) uses a low-frequency component. Once the source and target witnesses are high, the compressed crossing has exactly the same matrix coefficient as the full crossing, which is (13). Thus the same min--max argument used in PF-226 applies after subtracting only the finite/slowly growing low-frequency codimension.

## 3. Relation to the weak-trace endpoint

PF-226 left two possible ways for the PF-212 split to help with the inverse-seam channel count: it could remove most channels by rank truncation, or it could leave the channels present but damp them quantitatively through the high-frequency Poisson/resolvent factors. PF-227 rules out the first mechanism for every cutoff satisfying (8).

In particular, a fixed physical cutoff cannot turn the raw crossing into a uniformly finite-channel object. The high--high raw block itself has

\[
\mathfrak c_n^{\mathrm{hh}}
:=
\sum_k\min\left\{\frac12,
 s_k(H_{\kappa,n+1}B_nH_{\kappa,n})
\right\}
\ge \frac{c}{s_n}.
\tag{21}
\]

The same lower diagnostic as PF-226 therefore persists after fixed high-pass compression:

\[
\delta_n\mathfrak c_n^{\mathrm{hh}}
\ge
c\frac{g_n}{P_n(g_n+g_{n+1})}.
\tag{22}
\]

Equation (22) is still only a diagnostic for a raw saturated-mass triangle route. No convergence or divergence claim is made for its series.

The actual PF-212 theorem remains a live positive mechanism because its high-frequency factors carry **singular-value decay**, e.g. the energy-normalized Poisson factor has

\[
s_j(M(I-P_\kappa))
\le
\frac{CL}{j+c\kappa L}.
\tag{23}
\]

PF-227 says that this quantitative decay, or comparable damping supplied by the resolvent contractions in PF-225,

\[
X_n=-(F_nDF_n)B_n(E_nD^{(n)}E_n),
\tag{24}
\]

must actually be used. Merely declaring the PF-226 band to be "high frequency" does not reduce its multiplicity.

## 4. Prior art and novelty audit

No novelty is claimed for the linear-algebra ingredients: finite-codimension intersection, compression, and singular-value min--max are standard. The only durable project-specific content is their application to the exact PF-226 thin-pant witness band together with the exact PF-212 physical Fourier rank scale.

Hislop and Lutzer, *Spectral Asymptotics of the Dirichlet-To-Neumann Map on Multiply Connected Domains in R^d*, **Inverse Problems 17** (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`, show that for a fixed smooth multiply connected domain the off-diagonal Dirichlet-to-Neumann coupling is smoothing at high energy. That fixed-geometry statement does not give a uniform bound when the relevant boundary components approach at scale `s_n`, and therefore does not contradict (17).

Bucur, Henrot, and Michetti, *Asymptotic behaviour of the Steklov spectrum on dumbbell domains*, **Communications in Partial Differential Equations 46** (2021), 362--393, DOI `10.1080/03605302.2020.1840587`, show that thin-domain Steklov degeneration can have nontrivial lower-dimensional spectral limits. Their problem does not identify the PF boundary-energy-normalized off-diagonal crossing or the high--high compressed channel count (17).

A fresh targeted search over thin-domain Steklov/DtN asymptotics, collapsing boundary components, and high-frequency off-diagonal DtN coupling did not identify a theorem directly giving or forbidding the PF statement (17). The claim is therefore classified as an exact specialization/combination of the already-persisted PF-212 and PF-226 mechanisms, not as a new general theorem about Dirichlet-to-Neumann maps.

## 5. Falsification and boundary checks

1. The argument never assumes that the PF-226 normal-ray map `J_n` preserves Fourier frequency. Source and target high-pass conditions are separate finite-codimension constraints.
2. The low-sector rank is charged on **both** modules. Omitting the target rank would not justify the high--high compression.
3. The threshold `\tau` is inherited from the same uniform PF-226 norm comparison after restriction to a subspace; no new lower bound on strip DtN eigenvalues is introduced.
4. The varying-cutoff extension requires (8). A cutoff of order `1/(s_nL_n)` or larger is outside the theorem and could consume a macroscopic fraction of the witness space by dimension alone.
5. The BHP exponent is used only for the convenient sufficient growth condition (20). The intrinsic statement is (8), which depends on the exact local seam scale and cuff lengths.
6. Equation (17) concerns the **raw** high--high crossing. It gives no lower bound on the dressed flux `X_n`, `[D,E_n]`, `P[D,E_n]H`, or the final relative resolvent.
7. PF-212's strong/weak endpoint estimates for Poisson-recouping words are not weakened. They use singular-value decay of normalized extension factors, not finite rank of the high sector.
8. No divergence is asserted for the weighted diagnostic (22), and no failure of weak `S_1` is inferred.
9. Nothing here addresses the independent PF-204 unsmoothed route, the PF-183 short-collar splice, wave operators, determinants/resonances, prime/clone separation, or an RH implication.

## Consequences for the research line

PF-224 rules out reciprocal-prime weighting of the **raw amplitude**, PF-225 shows that resolvent inversion saturates amplitude and moves attention to channel count, and PF-226 proves that the canonical thin pant supplies an inverse-seam number of raw saturated channels. PF-227 now shows that these channels do not disappear under the PF-212 physical low/high split: after deleting every fixed or sufficiently slowly growing physical-frequency sector, order `s_n^{-1}` of them remain in the raw high--high crossing.

The smooth weak-trace route is therefore narrowed one step further. A positive continuation must exploit the quantitative singular-value decay of the PF-212 high-frequency Poisson factors **inside** the actual dressed/reassembled word, or prove comparable suppression by the two contractions in (24). A negative continuation must show that enough of the high--high band survives those quantitative factors. Pure rank truncation, low-sector counting, fixed-edge smoothing, raw-amplitude saturation, and raw high-pass compression are now all below the decisive threshold.